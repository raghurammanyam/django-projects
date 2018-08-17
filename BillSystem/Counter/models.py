from django.db import models
import datetime

# Create your models here.
class Inventory(models.Model):
    Rs2000 = models.IntegerField(default=0)
    Rs500 = models.IntegerField(default=0)
    Rs200 = models.IntegerField(default=0)
    Rs100 = models.IntegerField(default=0)
    Rs50 = models.IntegerField(default=0)
    Rs10 = models.IntegerField(default=0)
    Rs5 = models.IntegerField(default=0)
    Rs2 = models.IntegerField(default=0)
    Rs1 = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now = True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return '%d,%d,%d,%d,%d,%d,%d,%d,%d,%d'%(self.id,self.Rs2000,self.Rs500,self.Rs200,self.Rs100,self.Rs50,self.Rs10,self.Rs5,self.Rs2,self.Rs1)
    def as_dict(self):
        return {
            "Rs2000":self.Rs2000,"Rs500":self.Rs500,"Rs200":self.Rs200,"Rs100":self.Rs100,"Rs50":self.Rs50,"Rs10":self.Rs10,"Rs5":self.Rs5,"Rs2":self.Rs2,"Rs1":self.Rs1}


class Bill(models.Model):
    bill=models.IntegerField(default=0)
    amount=models.IntegerField()
    change=models.IntegerField(default=0)
    Rs2000 = models.IntegerField()
    Rs500 = models.IntegerField()
    Rs200 = models.IntegerField()
    Rs100 = models.IntegerField()
    Rs50 = models.IntegerField()
    Rs10 = models.IntegerField()
    Rs5 = models.IntegerField()
    Rs2 = models.IntegerField()
    Rs1 = models.IntegerField()
    created = models.DateTimeField(auto_now = True)

    def __str__(self):
        return '%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d'%(self.bill,self.amount,self.change,self.Rs2000,self.Rs500,self.Rs200,self.Rs100,self.Rs50,self.Rs10,self.Rs5,self.Rs2,self.Rs1)
    def as_dict(self):
        return {
            "Rs2000":self.Rs2000,"Rs500":self.Rs500,"Rs200":self.Rs200,"Rs100":self.Rs100,"Rs50":self.Rs50,"Rs10":self.Rs10,"Rs5":self.Rs5,"Rs2":self.Rs2,"Rs1":self.Rs1}
