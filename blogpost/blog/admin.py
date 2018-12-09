from django.contrib import admin
from .models import post,comment

# Register your models here.
class postDetail(admin.ModelAdmin):
    list_display = ('title','slug','author','publish','status')
    list_filter =('author','created','publish','author')
    search_fields = ('title','body')
    prepopulated_fields ={"slug":('title',)}
    raw_id_fields =('author',)
    date_hierarchy = 'publish'
    ordering = ('status','publish')
admin.site.register(post,postDetail)

class commentDetail(admin.ModelAdmin):
    list_display = ('name','email','post','active','created')
    list_filter =('post','created','updated')
    search_fields = ('name','email','body')
admin.site.register(comment,commentDetail)
