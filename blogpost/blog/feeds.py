from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import post


class Latestpostfeed(Feed):
    title = "My blog"
    link = '/blog/'
    description = 'new posts of my blog'
    def items(self):
        return post.published.all()
    def item_title(self,item):
        return item.title
    def item_description(self,item):
        return truncatewords(item.body,10)
