from django.urls import path,reverse
from django.conf.urls import url
from blog.templatetags.blog_tags import total_posts
from blog.feeds import Latestpostfeed

from .views import getpost
app_name	=	'blog'

urlpatterns = [
 path('get',total_posts),
 url(r'^post/$',getpost,name='getpost'),
 path('feed',Latestpostfeed(),name='post-feed'),

 ]
