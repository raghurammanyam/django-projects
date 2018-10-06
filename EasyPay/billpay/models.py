from django.db import models
from djchoices import DjangoChoices, ChoiceItem



class users(models.Model):
    name=models.CharField(max_length=50)
    mobile_no =models.CharField(max_length=10)
    address=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)


class transactions(models.Model):
    #class choice(DjangoChoices):
    paid= "paid"
    not_paid = "not_paid"
    choice = ((paid,'paid'),
                (not_paid,'not_paid'))
    user=models.ForeignKey(users,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12,decimal_places=2)
    #remaing_balance = models.DecimalField(max_digits=12,decimal_places=2,blank=True,null=True)
    status = models.CharField(max_length=10,choices=choice,default=not_paid,blank=True)
    partial_status=models.NullBooleanField()
    payment_type =models.CharField(max_length=30,default=None,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "%d,%f,%s,%s,%s,%s"%(self.id,self.amount,self.status,self.partial_status,self.created_at,self.updated_at)
    def as_dict(self):
        return {"user":self.user,"amount":self.amount,"status":self.status,"partial_status":self.partial_status,"created_at":self.created_at,"updated_at":self.updated_at}


class payments(models.Model):
    user=models.ForeignKey(users,on_delete=models.CASCADE,default=None,blank=True)
    transaction = models.ForeignKey(transactions,on_delete=models.CASCADE,default=None,blank=True,null=True)
    payment_amount = models.DecimalField(max_digits=12,decimal_places=2)
    pay_via =models.CharField(max_length=30)
    pay_status = models.BooleanField(default=True)
    partial_amount=models.DecimalField(max_digits=12,decimal_places=2,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class user_credits(models.Model):
    user=models.ForeignKey(users,on_delete=models.CASCADE,default=None,blank=True)
    transaction = models.ForeignKey(transactions,on_delete=models.CASCADE,default=None,blank=True,null=True)
    payment = models.ForeignKey(payments,on_delete=models.CASCADE,default=None,blank=True,null=True)
    extra_amount = models.DecimalField(max_digits=12,decimal_places=2,blank=True)
    status = models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



# Create your models here.
