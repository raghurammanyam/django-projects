from django.db import models

#This function is used to save the images of the Carosuel
def image1(instance,filename):
    return 'images/{0}{1}'.format(get_random_string(length=100), filename)

#This function is used to save the images of the Categories
def image2(instance,filename):
    return 'images/{0}{1}'.format(get_random_string(length=100), filename)

#This function is used to save the images of the CategoryCarosuel
def image3(instance,filename):
    return 'images/{0}{1}'.format(get_random_string(length=100), filename)

#This function is used to save the images of the CategoryList
def image4(instance,filename):
    return 'images/{0}{1}'.format(get_random_string(length=100), filename)

#This function is used to save the images of the CategoryListImages
def image5(instance,filename):
    return 'images/{0}{1}'.format(get_random_string(length=100), filename)


class Roles(models.Model):
    name = models.CharField(max_length=30)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Users(models.Model):
    role=models.ForeignKey(Roles,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mobile_no = models.CharField(max_length=13)
    address =  models.TextField()
    emailId = models.EmailField(blank=True,unique=True)
    password = models.CharField(max_length=500)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class MainPageCarousel(models.Model):
    carouselname = models.CharField(max_length=30)
    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Carousel(models.Model):
    slide = models.ImageField(upload_to='image1',blank=True,null=True)
    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    carouselname = models.ForeignKey(MainPageCarousel,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Categories(models.Model):
    category = models.CharField(max_length=30)
    image = models.ImageField(upload_to='image2',blank=True,null=True)
    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CategoryCarousel(models.Model):
    category = models.ForeignKey(Categories,on_delete=models.CASCADE)
    slide = models.ImageField(upload_to='image3',blank=True,null=True)
    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CategoryList(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=13)
    email = models.EmailField(blank=True, default="")
    description = models.TextField()
    images = models.ImageField(upload_to='image4',blank=True,null=True)
    category = models.ForeignKey(Categories,on_delete=models.CASCADE)
    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    address = models.TextField()
    status = models.BooleanField(default=True)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CategoryListImages(models.Model):
    list = models.ForeignKey(CategoryList,on_delete=models.CASCADE)
    images = models.ImageField(upload_to='image5',blank=True,null=True)
    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
