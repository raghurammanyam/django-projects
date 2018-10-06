
from django.conf.urls import url
from django.urls import path
from .views import test,get
from django.http import HttpResponse

urlpatterns = [

    url(r'^date/',test),
    url(r'^get/',get)

]
