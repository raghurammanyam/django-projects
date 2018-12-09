from django.shortcuts import render
from .models import post
from django.http import JsonResponse,HttpResponse
from django.forms.models import model_to_dict
from rest_framework.reverse import reverse

def getpost(request):
    all=post.published.all()
    context={"data":reverse(args=list(all),request=request)}
    print(context)
    #c=model_to_dict(all)
    #print(c)
    return JsonResponse({"data":context})
# Create your views here.
