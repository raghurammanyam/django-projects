from django.contrib import admin
from .models import Users,Categories,categorie_curosels,Carousels,List_Of_Items,Item_Pics,MainPage,Roles


class RolesDetails(admin.ModelAdmin):
    list_display=('Name','status')
admin.site.register(Roles,RolesDetails)

class UsersDetails(admin.ModelAdmin):
    list_display = ('First_name','Last_name','Mobile_no','Email')
admin.site.register(Users,UsersDetails)

class MainpageDetails(admin.ModelAdmin):
    list_display = ('Name','status')
admin.site.register(MainPage,MainpageDetails)
class CarouselsDetails(admin.ModelAdmin):
    list_display = ('mainpage','carousel','status')
admin.site.register(Carousels,CarouselsDetails)

class CategoriesDetails(admin.ModelAdmin):
    list_display = ('name','description','pics')
admin.site.register(Categories,CategoriesDetails)

class categorie_curoselsDetails(admin.ModelAdmin):
    list_display = ('categorie','carousel')
admin.site.register(categorie_curosels,categorie_curoselsDetails)

class List_Of_ItemsDetails(admin.ModelAdmin):
    list_display = ('Categorie','Name','Banner')
admin.site.register(List_Of_Items,List_Of_ItemsDetails)

class Item_PicsDetails(admin.ModelAdmin):
    list_display = ('Item','photos')
admin.site.register(Item_Pics,Item_PicsDetails)
# Register your models here.
