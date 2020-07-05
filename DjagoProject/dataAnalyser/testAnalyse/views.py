from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import NotifyUsers

from firebase import firebase  
import json

firebase = firebase.FirebaseApplication('https://mobilecomputing-4788c.firebaseio.com/', None) 

def index(request):
    return HttpResponse("<center><h1>Welcome To Patil's World..</h1></center>")
    
#http://13.233.129.21:8000/addNotifyUsers?email=Abhi@gmail.com&high=100&low=10&company=MSFT
def addNotifyUsers(req):
    
    email=req.GET['email']
    high=req.GET['high']
    low=req.GET['low']
    company=req.GET['company']
    
    db=NotifyUsers(email=email,high=high,low=low,company=company)
    db.save()
    
    print("New User added : ",email)
    
    return JsonResponse({"status":200}) 

msgHIGH="Best Time To Sell"
msgLOW="Best Time TO Buy"

def sendNotifyUsers(req):
    
    li=['AAPL','AMZN','GOOGL','MSFT']
    
    #alertUsers= firebase.get('/pushNotify/'+i+'/','')
    
    stocksPrice={}
    
    companies=['MSFT','AAPL','GOOGL','AMZN']
    
    for comp in companies:
        result = firebase.get('/Stocks/'+comp+'/', '')  
        price=result['data']['y']
        
        stocksPrice[comp]=price
        
        #print(result,price)
    
    print(stocksPrice)
    
    for comp in companies:
        users=NotifyUsers.objects.filter(company=comp)
        #print(comp)
        for user in users:
            print(user)
            if user.high < stocksPrice[comp]:
                sendEmail("HIGH",user.email,comp)
            
            elif user.low > stocksPrice[comp]:
                sendEmail("LOW",user.email,comp)
            
    return JsonResponse({"status":200})

def sendEmail(state,to,comp):
    
    if state=="HIGH":
        msg=msgHIGH
    else:
        msg=msgLOW
    msg+=" "+comp+" Stocks"
    
    print("Email Sent : ",msg," To ",to)
    
    try:
        import smtplib 
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls() 
        s.login("Abhishekspatil92@gmail.com", open("/home/ec2-user/environment/MobileComputing/DjagoProject/dataAnalyser/testAnalyse/passwords/password.txt", "r").read()) 
        s.sendmail("Abhishekspatil92@gmail.com", to, msg)
        s.quit()
        
        print("Sent Email")
    except Exception as e:
        print(e) 
        print("Some Error Happened Sending Email.. Try again or Contact Patil92")
        
    
                
    
    
    
    
    




