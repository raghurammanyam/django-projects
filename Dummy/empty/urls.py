from django.urls import path
from django.conf.urls import url
from .views import Bot
from .restapi import createuser
urlpatterns = [
    path('get',Bot.as_view()),
    path('post',createuser.as_view())
]
