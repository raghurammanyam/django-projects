from django.contrib.sitemaps import Sitemap
from .models import *



class postSitemap(Sitemap):
    changefreq ='weekly'
    priority = 0.9

    def items(self):
        return post.published.all()
    def	lastmod(self,obj):
        return obj.updated
