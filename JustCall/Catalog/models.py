from django.db import models
from django.utils.crypto import get_random_string

import crypt
def new_file_name(instance, filename):
    return 'images/{0}{1}'.format(get_random_string(length=10), filename)
def list_file_name(instance, filename):
    return 'banner/{0}{1}'.format(get_random_string(length=10), filename)
def carosule_file_name(instance, filename):
    return 'carosulepic/{0}{1}'.format(get_random_string(length=10), filename)
def cat_file_name(instance, filename):
    return 'categpic/{0}{1}'.format(get_random_string(length=10), filename)
def item_file_name(instance, filename):
    return 'item_pics/{0}{1}'.format(get_random_string(length=10), filename)


class Roles(models.Model):
    Name = models.CharField(max_length=50)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return "%s"%(self.Name)

class Users( models.Model):
    role = models.ForeignKey(Roles,on_delete=models.CASCADE)
    First_name = models.CharField(max_length=20)
    Last_name = models.CharField(max_length=20)
    Password = models.CharField(max_length=255)
    Mobile_no = models.CharField(max_length=20)
    Email = models.CharField(max_length=50)
    Address = models.TextField()
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
         return self.First_name + ' ' + self.Last_name
    def __str__(self):
        return "%s,%s"%(self.Mobile_no,self.Email)

class MainPage(models.Model):
    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    Name = models.CharField(max_length=50)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return "%s"%(self.Name)
class Carousels(models.Model):
    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    mainpage = models.ForeignKey(MainPage,on_delete=models.CASCADE)
    carousel = models.ImageField(upload_to=carosule_file_name,blank=True,null=True)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now = True)
    #def __str__(self):
        #return  "%s"  %(self.staus)



class Categories(models.Model):
    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    description = models.TextField()
    mobile_no = models.CharField(max_length=20)
    pics = models.ImageField(upload_to=new_file_name,blank=True,null=True)
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now = True)
    status = models.BooleanField()

    def __str__(self):
        return  "%s"  %(self.name)


class categorie_curosels(models.Model):
    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categories,on_delete=models.CASCADE)
    carousel = models.ImageField(upload_to=cat_file_name,blank=True,null=True)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now = True)


class List_Of_Items(models.Model):
    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    Categorie = models.ForeignKey(Categories,on_delete=models.CASCADE)
    Name = models.CharField(max_length=50)
    Mobile_no = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Banner = models.ImageField(upload_to=list_file_name,blank=True,null=True)
    Address = models.TextField()
    Description = models.TextField()
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.Name + '- ' + self.Mobile_no


class Item_Pics(models.Model):
    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    Item = models.ForeignKey(List_Of_Items,on_delete=models.CASCADE)
    photos = models.ImageField(upload_to=item_file_name,blank=True,null=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now = True)
