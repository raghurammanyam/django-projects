from django.conf.urls import include,url
from onorapp.Controllers.Roles import getUpdateRoles
from onorapp.Controllers.PostRoles import addRoles
from onorapp.Controllers.User import getUpdateDeleteUsers
from onorapp.Controllers.PostUsers import addUsers
from onorapp.Controllers.MainPageCarousel import getUpdateDeleteMainPageCarousel
from onorapp.Controllers.PostMainPageCarousel import addMainPageCarousel
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


urlpatterns=[
     url(r'^getupdateroles/(?P<id>[0-99]+)/$',getUpdateRoles.as_view()),
     url(r'^addroles',addRoles.as_view()),
     url(r'^getupdatedeleteusers/(?P<id>[0-99]+)/$',getUpdateDeleteUsers.as_view()),
     url(r'^addusers',addUsers.as_view()),
     url(r'^getupdatedeletemainpagecarousel/(?P<id>[0-99]+)/$',getUpdateDeleteMainPageCarousel.as_view()),
     url(r'^addmainpagecarousel',addMainPageCarousel.as_view()),
     url(r'^getupdatedeletecarousel/(?P<id>[0-99]+)/$',getUpdateDeleteCarousel.as_view()),
     url(r'^addcarousel',addCarousel.as_view()),
     url(r'^getupdatedeletecategories/(?P<id>[0-99]+)/$',getUpdateDeleteCategories.as_view()),
     url(r'^addcategories',addCategories.as_view()),
     url(r'^getupdatedeletecategorycarousel/(?P<id>[0-99]+)/$',getUpdateDeleteCategoryCarousel.as_view()),
     url(r'^addcategorycarousel',addCategoryCarousel.as_view()),
     url(r'^getupdatedeletecategorylist/(?P<id>[0-99]+)/$',getUpdateDeleteCategoryList.as_view()),
     url(r'^addcategorylist',addCategoryList.as_view()),
     url(r'^getupdatedeleteitemimages/(?P<id>[0-99]+)/$',getUpdateDeleteItemImages.as_view()),
     url(r'^additemimages',createItemImages.as_view()),

]
