from django.db import models

class users(models.Model):
    name =models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=10)
    
class user_transactions(models.Model):
    name = models.CharField(max_length=20)
    mobile_no = models.CharField(max_length=10)
    address = models.TextField()
    transaction_amount=models.DecimalField(max_digits=12,decimal_places=2)


# Create your models here.
