from django.db import models
from django.utils import timezone


class BlogPost(models.Model):
    name = models.CharField(max_length = 40)
    job = models.CharField(max_length = 44)
    email = models.CharField(max_length = 55)
