
from firebase import firebase  
firebase = firebase.FirebaseApplication('https://mobilecomputing-4788c.firebaseio.com/', None) 
  
  
def PushNotify():
    
    result = firebase.get('/pushNotify/', '')
    
    for i in result:
        print(i)
        
    #print(result) 

PushNotify()

def sendEmail(to,st):
    
    try:
        import smtplib 
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls() 
        s.login("Abhishekspatil92@gmail.com", open("/home/ubuntu/environment/KafkaDjangoServer/kafkaApp/password.txt", "r").read()) 
        s.sendmail("Abhishekspatil92@gmail.com", to, st)
        s.quit()
        
        print("Sent Email")
    except Exception:
        print("Some Error Happened Sending Email.. Try again or Contact Patil92")
        
