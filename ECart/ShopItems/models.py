from django.db import models


class Customers(models.Model):

    name = models.CharField(max_length=60)
    Address = models.TextField()
    mobile_no = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return  "%s"  %(self.name)


class categories(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now = True)
    updated = models.DateTimeField(auto_now = True)
    status = models.BooleanField()
    def __str__(self):
        return "%s" %(self.name)





class Items(models.Model):

    name = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    Description =models.TextField()
    created = models.DateTimeField(auto_now = True)
    updated = models.DateTimeField(auto_now = True)
    catogorie = models.ForeignKey(categories,on_delete=models.CASCADE)
    status = models.BooleanField()

    def __str__(self):
        return  "%s" %(self.name)




class Orders(models.Model):

    Item = models.ForeignKey(Items,on_delete = models.CASCADE)
    cust = models.ForeignKey(Customers,on_delete=models.CASCADE)
    catogorie = models.ForeignKey(categories,on_delete=models.CASCADE)
    Total_price = models.DecimalField(max_digits=10,decimal_places=2)
    Status = models.BooleanField()
    created = models.DateTimeField(auto_now = True)
    updated = models.DateTimeField(auto_now = True)






# Create your models here.
