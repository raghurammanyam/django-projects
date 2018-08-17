from django.conf.urls import url,include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .restapi import post,cust,pro,ord,get,call,cat,apt,put,oak,update,tes,dele,sat,gan,bas
from .views import asn,fun,ram,price,hat,bot,lab,can,rank,tac,part,nat,wir,mar,cost,app,activate,signup
from .classapi import List,Bull,Detail,Rossum,Van,Dell,Key,Pad
from django.contrib.auth import views as auth_views

urlpatterns =[

   path('post',post),
   path('cust',cust),
   path('pro',pro),
   path('ord',ord),
   url(r'^get/(?P<_id>\d+)',get),
   url(r'^cat/(?P<_id>\d+)',cat),
   url(r'^call/(?P<_id>\d+)',call),
   path('apt',apt),
   url(r'^put/(?P<_name>[\w\-]+)/$',put),
   url(r'^update/(?P<_name>[\w\-]+)/$',update),
   url(r'^oak/(?P<_name>[\w\-]+)/$',oak),
   url(r'^tes/(?P<_id>\d+)',tes),
   url(r'^dele/(?P<_id>\d+)',dele),
   url(r'^sat/(?P<_id>\d+)',sat),
   url(r'^gan/(?P<_id>\d+)',gan),
   url(r'^bas/(?P<_id>\d+)',bas),

   #views
   url(r'^asn/',asn),
   url(r'^fun/',fun),
   url(r'^ram/',ram),
   url(r'^price/',price),
   url(r'^hat/(?P<_name>[\w\-]+)/$',hat),
   url(r'^bot/(?P<_range>[0-99,-]+)',bot),
   url(r'^lab/(?P<_range>[0-99,-]+)',lab),
   url(r'^can/(?P<_name>[\w\-]+)/$',can),
   url(r'^rank',rank),
   url(r'^tac/(?P<_price>[0-99,-]+)',tac),
   url(r'^part/(?P<_name>[\w\-]+)/$',part),
   url(r'^nat/(?P<_id>\d+)',nat),
   url(r'^wir/(?P<_status>[\w\-]+)/$',wir),
   url(r'^mar/',mar),
   url(r'^cost/',cost),
   url(r'^app/',app),
   #classapi
   path('list',List.as_view()),
   path('bull',Bull.as_view()),
   url(r'^det/(?P<id>\d+)',Detail.as_view()),
   url(r'rossum/(?P<id>\d+)',Rossum.as_view()),
   url(r'van/(?P<id>\d+)',Van.as_view()),
   url(r'dell/(?P<id>\d+)',Dell.as_view()),
   url(r'key/(?P<id>\d+)',Key.as_view()),
   path('pad',Pad.as_view()),
   path('rest-auth/', include('rest_auth.urls')),
   path('rest-auth/registration/', include('rest_auth.registration.urls')),
   url(r'^signup/$',signup, name='signup'),
   url(r'^activate/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),
   ]
urlpatterns = format_suffix_patterns(urlpatterns)
