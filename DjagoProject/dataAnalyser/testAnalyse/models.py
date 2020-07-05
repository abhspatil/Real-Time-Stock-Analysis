from django.db import models

# Create your models here.

class NotifyUsers(models.Model):
    
    email=models.EmailField()
    high=models.IntegerField(default=0)
    low=models.IntegerField(default=0)
    company=models.CharField(max_length =20)

