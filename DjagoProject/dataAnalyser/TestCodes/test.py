
'''from alpha_vantage.timeseries import TimeSeries

ts = TimeSeries(key='S2B09JXEQGMV0XQD', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT',interval='60min', outputsize='full')

print(data.head(20))
print(len(data))

def getStocksData(l):
    from alpha_vantage.timeseries import TimeSeries
    
    ts = TimeSeries(key='S2B09JXEQGMV0XQD', output_format='pandas')
    
    for company in l:
        data, meta_data = ts.get_intraday(symbol=company,interval='60min', outputsize='full')
        
        data=data['4. close']
        
        #data.to_csv("stocks_csv/"+company+".csv",index = None,header=True)
        data.to_csv(company+".csv",index = None,header=False)
        
        print(company,"Data Got Successfully..")

def pushStockDataFireBase(li):
    
    from firebase import firebase  
    firebase = firebase.FirebaseApplication('https://mobilecomputing-4788c.firebaseio.com/', None) 
        
    import time
    for cmp in li:
        f = open(cmp+".csv", "r")
        cnt=0
        for i in f:
            #print(i)
            #time.sleep(1)
            
            data =  { 'x': cnt,  
                      'y': float(i.replace("\n","")),  
                    }  
            
            try:
                result = firebase.post('/GOGL/',data)
                firebase.put('/Stocks/GOGL/','data',data)
            except:
                return
            
            
            print(result,"Set Successfully")  
            cnt+=1


    

stocks=['MSFT','GOOGL','AAPL']
#getStocksData(stocks)

pushStockDataFireBase(['GOOGL'])



def getStocksData(l):
    from alpha_vantage.timeseries import TimeSeries
    
    ts = TimeSeries(key='S2B09JXEQGMV0XQD', output_format='pandas')
    
    for company in l:
        data, meta_data = ts.get_intraday(symbol=company,interval='60min', outputsize='full')
        
        data=data['4. close']
        
        data.to_csv("stocks_csv/"+company+".csv",index = None,header=True)

stocks=['AAPL','GOGL','MSFT']
getStocksData(stocks)


def getAlerts(li):
    
    from firebase import firebase  
    import json
    
    firebase = firebase.FirebaseApplication('https://mobilecomputing-4788c.firebaseio.com/', None) 
    
    for comp in li:
        result = firebase.get('/Stocks/'+comp+'/', '')  
        price=result['data']['y']
        
        print(result,price)
        
        
        alertUsers= firebase.get('/pushNotify/'+comp+'/','')
        
        if alertUsers is not None:
            
            for user in alertUsers:
                print(user[0],user[1],user[2])
            
        #print(alertUsers)
        print()
        


li=['AMZN','AAPL','MSFT','GOOGL']
getAlerts(li)
'''

from firebase import firebase  
import json

firebase = firebase.FirebaseApplication('https://mobilecomputing-4788c.firebaseio.com/', None) 


alertUsers= firebase.get('/pushNotify/'+'GOGL'+'/','')
alertUsers=json.dumps(alertUsers)
alertUsers=json.loads(alertUsers)

print(alertUsers)
if alertUsers is not None:
    
    for user in alertUsers:
        user=json.dumps(user)
        user=json.loads(user)
        for u in user:
            print(u)


                
    