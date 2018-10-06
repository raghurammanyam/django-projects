from django.db import models
from django.utils.crypto import get_random_string
def sport_file_name(instance, filename):
    return 'images/{0}{1}'.format(get_random_string(length=10), filename)


class sports(models.Model):
    name = models.CharField(max_length=50)
    event_date = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(upload_to=sport_file_name,blank=True,null=True)
    status = models.BooleanField()

class player(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    sport = models.ForeignKey(sports,on_delete=models.CASCADE)

# Create your models here.
