from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.http import StreamingHttpResponse
import mongoengine
from mongoengine import *
from .models import Address
def test(request):
    connect("test")
    a=Address(name="raghu",email='ram@gmail.com')
    a.save()
    return HttpResponse("yes its saved")
    #user = connect(username=ram,password=Raghuram@9)
    #assert isinstance(user,mongoengine.django.auth.User)
    #name = Address.objects(name__contains="ram").first()
    #email = Address.objects(email__contains="manyam@gmail.com")
    #name.email.append(Address)
    #Address.save()

    #print Address.name
def get(request):
    connect("test")
    dat = Address.objects.all()
    context = {'dat':list(dat)}
    print (list(dat))
    return HttpResponse(dat)
