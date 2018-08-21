from django.conf.urls import include,url
from onorapp.Controllers.Roles import getUpdateRoles
from onorapp.Controllers.PostRoles import addRoles
from onorapp.Controllers.User import getUpdateDeleteUsers
from onorapp.Controllers.PostUsers import addUsers
from onorapp.Controllers.Carousel import getUpdateDeleteCarousel
from onorapp.Controllers.PostCarousel import addCarousel
from onorapp.Controllers.Categories import getUpdateDeleteCategories
from onorapp.Controllers.PostCategories import addCategories
from onorapp.Controllers.CategoryCarousel import getUpdateDeleteCategoryCarousel
from onorapp.Controllers.PostCategoryCarousel import addCategoryCarousel
from onorapp.Controllers.CategoryList import getUpdateDeleteCategoryList
from onorapp.Controllers.PostCategoryList import addCategoryList
from onorapp.Controllers.CategoryListImages import getUpdateDeleteItemImages
from onorapp.Controllers.PostCategoryListImages import createItemImages
from onorapp.Controllers.login_api import login
from onorapp.Controllers.getcategoriecarousel import getCategoryCarousel
from onorapp.Controllers.getcategorylist import getCategoryList
from onorapp.Controllers.getitemimages import getItemImages
from onorapp.Controllers.getstatusactive import getcategorystatus,getuserstatus,getrolesstatus
from onorapp.Controllers.getstatusactive import getcarouselstatus,getcategorycarouselstatus
from onorapp.Controllers.getstatusactive import getcategoryliststatus,getcategorylistimagestatus

urlpatterns=[
     url(r'^getupdateroles/(?P<id>\d+)$',getUpdateRoles.as_view()),
     url(r'^addroles',addRoles.as_view()),
     url(r'^getupdatedeleteusers/(?P<id>\d+)$',getUpdateDeleteUsers.as_view()),
     url(r'^addusers',addUsers.as_view()),
     url(r'^getupdatedeletecarousel/(?P<id>\d+)$',getUpdateDeleteCarousel.as_view()),
     url(r'^addcarousel',addCarousel.as_view()),
     url(r'^getupdatedeletecategories/(?P<id>\d+)$',getUpdateDeleteCategories.as_view()),
     url(r'^addcategories',addCategories.as_view()),
     url(r'^getupdatedeletecategorycarousel/(?P<id>\d+)$',getUpdateDeleteCategoryCarousel.as_view()),
     url(r'^addcategorycarousel',addCategoryCarousel.as_view()),
     url(r'^getupdatedeletecategorylist/(?P<id>\d+)$',getUpdateDeleteCategoryList.as_view()),
     url(r'^addcategorylist',addCategoryList.as_view()),
     url(r'^getupdatedeleteitemimages/(?P<id>\d+)$',getUpdateDeleteItemImages.as_view()),
     url(r'^additemimages',createItemImages.as_view()),
     url(r'^getcategorycarousel/(?P<id>\d+)$',getCategoryCarousel.as_view()),
     url(r'^getcategorylist/(?P<id>\d+)$',getCategoryList.as_view()),
     url(r'^getitemimages/(?P<id>\d+)$',getItemImages.as_view()),
     url(r'^getcategorystatus',getcategorystatus.as_view()),
     url(r'^getuserstatus',getuserstatus.as_view()),
     url(r'^getrolesstatus',getrolesstatus.as_view()),
     url(r'^getcarouselstatus',getcarouselstatus.as_view()),
     url(r'^getcategorycarouselstatus',getcategorycarouselstatus.as_view()),
     url(r'^getcategoryliststatus',getcategoryliststatus.as_view()),
     url(r'^getcategorylistimagestatus',getcategorylistimagestatus.as_view()),
     url(r'^login',login.as_view()),


]
