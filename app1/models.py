from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):

    address = models.CharField(max_length=30)
    def __str__(self):
        return self.username
    
        
class Financialdata(models.Model):
    acc_id = models.AutoField(primary_key=True)
    acc_holder = models.CharField(max_length=30)
    #user = models.ForeignKey(CustomeUser, on_delete=models.CASCADE)
    Acc_type = models.CharField(max_length=30, choices = [('saving','saving'),('checking','checking'),('investment','investment')])
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return self.acc_holder
    

class Analytics(models.Model):
    financialdata = models.ForeignKey(Financialdata, on_delete= models.CASCADE)
    profit = models.DecimalField(max_digits=10, decimal_places=2)
    revenue = models.DecimalField(max_digits =10, decimal_places=2)

    def __str__(self):
        return self.financialdata


