from django.conf.urls import url,include
from django.urls import path
from Catalog.Controllers.Usersapi import CreateUser
from Catalog.Controllers.carouselapi import CreateCarousel
from Catalog.Controllers.categorieapi import CreateCategorie
from Catalog.Controllers.categoriecarouselapi import CreateCategoriecarusel
from Catalog.Controllers.categorieupdateapi import getUpdateDeleteCategorie
from Catalog.Controllers.Userupdateapi import getUpdateDeleteUser
from Catalog.Controllers.categoriecarouselupdateapi import getUpdateDeleteCategorieCarousel
from Catalog.Controllers.carouselupdateapi import getUpdateDeleteCarousel
from Catalog.Controllers.ListItemapi import CreateItem
from Catalog.Controllers.listitemupdateapi import getUpdateDeleteItem
from Catalog.Controllers.itempicapi import CreateItemPic
from Catalog.Controllers.itempicupdateapi import getUpdateDeleteItemPic
from Catalog.Controllers.mainpageapi import CreateMainpage
from Catalog.Controllers.mainpageupdateapi import getUpdateDeleteMainpage
from Catalog.Controllers.rolesapi import CreateRoles
from Catalog.Controllers.rolesupdateapi import getUpdateRole
#from .views import send
urlpatterns = [
    path('createuser',CreateUser.as_view()),
    path('Createcarousel',CreateCarousel.as_view()),
    path('createcategorie',CreateCategorie.as_view()),
    url(r'^updatecategorie/(?P<id>\d+)',getUpdateDeleteCategorie.as_view()),
    path('createcategoriecarusel',CreateCategoriecarusel.as_view()),
    url(r'^updateuser/(?P<id>\d+)',getUpdateDeleteUser.as_view()),
    url(r'^updatecategoriecarusel/(?P<id>\d+)',getUpdateDeleteCategorieCarousel.as_view()),
    url(r'^updatecarusel/(?P<id>\d+)',getUpdateDeleteCarousel.as_view()),
    path('createitem',CreateItem.as_view()),
    url(r'^updateitem/(?P<id>\d+)',getUpdateDeleteItem.as_view()),
    path('createitemimage',CreateItemPic.as_view()),
    url(r'^updateitemimage/(?P<id>\d+)',getUpdateDeleteItemPic.as_view()),
    path('createmainpage',CreateMainpage.as_view()),
    url(r'^updatemainimage/(?P<id>\d+)',getUpdateDeleteMainpage.as_view()),
    path('createrole',CreateRoles.as_view()),
    url(r'^updaterole/(?P<id>\d+)',getUpdateRole.as_view()),
    #path('mail',send),



]
