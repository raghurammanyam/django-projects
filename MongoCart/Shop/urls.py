from django.conf.urls import url,include
from django.urls import path
from .views import Pad,Details

urlpatterns = [

  path('pad',Pad.as_view()),
  url(r'^details/(?P<status>[\w\-]+)/$',Details.as_view()),

]
