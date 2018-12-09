from	django import template
from blog.models import	post

from django.http import JsonResponse
from	django.utils.safestring	import	mark_safe
import	markdown

register = template.Library()
@register.filter(name='markdown')
def	markdown_format(text):
    return	mark_safe(markdown.markdown(text))
@register.simple_tag
def	total_posts(self):
    return	JsonResponse({"message":post.published.count()})
