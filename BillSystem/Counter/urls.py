from django.urls import path
from django.conf.urls import url
from  .restapi import Bot,update,like
from .views import Inven,cost,app,test,pay

urlpatterns = [
    path('get',Bot.as_view()),
    url(r'^update/(?P<id>\d+)',update),
    path('bill',like.as_view()),
    path('inv',Inven),
    path('cost/',cost),
    path('app/',app),
    url(r'^test/',test),
    url(r'^pay/',pay),
]
