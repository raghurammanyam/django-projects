from .views import sport,getplayer
from django.conf.urls import url
from django.urls import path


urlpatterns = [

   path('getsports',sport.as_view()),
   path('getplayer',getplayer.as_view()),
]
