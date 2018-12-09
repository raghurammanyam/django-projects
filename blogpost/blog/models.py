from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import	TaggableManager
from django.urls import reverse
#from .views import getpost

# Create your models here.
class publishedmanager(models.Manager):
    def get_queryset(self):
        return super(publishedmanager,self).get_queryset().filter(status='published')
class post(models.Model):
    STATUS_CHOICES = (('draft','Draft'),('published','Published'))
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    author =models.ForeignKey(User,on_delete=models.CASCADE,related_name = 'blog_posts')
    body = models.TextField()
    tags	=	TaggableManager()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='draft')
    objects	=	models.Manager()
    published = publishedmanager()

    class Meta:
        ordering =('-publish',)
    """def get_absolute_url(self):
        return reverse('blog:getpost', args=[self.publish.year,self.publish.month,self.publish.day,self.slug])"""
    def __str__(self):
        return '{} {} {} {} {} '.format(self.title,self.slug,self.publish,self.author,self.body)


class comment(models.Model):
    post = models.ForeignKey(post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=20)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
        ordering = ('created',)
    def __str__(self):
        return 'comment by {} on {}'.format(self.name,self.post)
