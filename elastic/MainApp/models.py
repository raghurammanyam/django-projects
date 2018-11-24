from django.db import models
from django.utils import timezone
#from django.contrib.auth.models import User
#from .search import BlogPostIndex

class BlogPost(models.Model):
   author = models.CharField(max_length = 50)
   posted_date = models.DateField('published')
   title = models.CharField(max_length=200)
   text = models.TextField(max_length=1000)

   """def indexing(self):
       obj = BlogPostIndex(
          meta={'id': self.id,'author':self.author,
          'posted_date':self.posted_date,
          'title':self.title,
          'text':self.text}

       )
       obj.save()
       return obj.to_dict(include_meta=True)"""
