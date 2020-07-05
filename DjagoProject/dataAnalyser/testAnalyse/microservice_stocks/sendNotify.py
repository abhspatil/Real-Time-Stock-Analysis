
import request
import time

def MonitorAlerts():
    
    while True:
        
        url="13.234.231.77:8000/sendNotifyUsers"
        x = requests.get(url)
        
        time.sleep(3)
        print("API Request made for Alerts")



    
    