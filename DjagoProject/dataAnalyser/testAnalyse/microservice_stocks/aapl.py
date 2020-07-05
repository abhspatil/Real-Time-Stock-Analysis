def getStocksData(l):
    from alpha_vantage.timeseries import TimeSeries
    print("API call for : ",l)
    
    ts = TimeSeries(key='5SIWA2DDI2ZPTICC', output_format='pandas')
    
    for company in l:
        data, meta_data = ts.get_intraday(symbol=company,interval='60min', outputsize='full')
        
        data=data['4. close']
        
        data.to_csv(company+".csv",index = None,header=False)

stocks=['AAPL','GOGL','MSFT']
#getStocksData(stocks)

def pushStockDataFireBase(li):
    
    from firebase import firebase  
    firebase = firebase.FirebaseApplication('https://mobilecomputing-4788c.firebaseio.com/', None) 
    
    print("Sending ",li,"Data")
    
    import time
    for cmp in li:
        f = open(cmp+".csv", "r")
        cnt=0
        for i in f:
            #print(i)
            
            
            data =  { 'x': cnt,  
                      'y': float(i.replace("\n","")),  
                    }  
            
            try:
                result = firebase.post('/'+cmp+'/',data)
                firebase.put('/Stocks/'+cmp+'/','data',data)
            except:
                return
        
            print(cmp,result,"Set Successfully")
            cnt+=1
            time.sleep(2)

pushStockDataFireBase(['AAPL']) 