from django.contrib import admin
from .models import Roles,Users,Categories,MainPageCarousel,Carousel,CategoryCarousel,CategoryList,CategoryListImages

class RolesDetails(admin.ModelAdmin):
    list_display=('name','status')
admin.site.register(Roles,RolesDetails)

class UserDetails(admin.ModelAdmin):
    list_display=('role','first_name','last_name','mobile_no','address','emailId','password','status')
admin.site.register(Users,UserDetails)

class MainPageCarouselDetails(admin.ModelAdmin):
    list_display=('carouselname','user','status')
admin.site.register(MainPageCarousel,MainPageCarouselDetails)

class CarouselDetails(admin.ModelAdmin):
    list_display=('slide','user','status','carouselname')
admin.site.register(Carousel,CarouselDetails)

class CategoryCarouselDetails(admin.ModelAdmin):
    list_display=('category','slide','user','status')
admin.site.register(CategoryCarousel,CategoryCarouselDetails)

class CategoriesDetails(admin.ModelAdmin):
    list_display=('category','image','user','status')
admin.site.register(Categories,CategoriesDetails)

class CategoryListDetails(admin.ModelAdmin):
    list_display=('name','mobile','email','description','images','category','user','status')
    search_fields=('category',)
admin.site.register(CategoryList,CategoryListDetails)

class CategoryListImagesDetails(admin.ModelAdmin):
    list_display=('list','images','user','status')
admin.site.register(CategoryListImages,CategoryListImagesDetails)
