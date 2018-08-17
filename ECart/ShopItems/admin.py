from django.contrib import admin
from .models import Customers,Items,Orders,categories

class CustomerDetails(admin.ModelAdmin):
    list_display = ('name','Address','mobile_no')
admin.site.register(Customers,CustomerDetails)

class categoriesDetails(admin.ModelAdmin):
    list_display = ('name','status')
admin.site.register(categories,categoriesDetails)

class ItemsDetails(admin.ModelAdmin):
    list_display = ('name','catogorie','price','status')
admin.site.register(Items,ItemsDetails)

class OrdersDetails(admin.ModelAdmin):
    list_display = ('id','cust','Item','catogorie','Total_price')
admin.site.register(Orders,OrdersDetails)


# Register your models here.
