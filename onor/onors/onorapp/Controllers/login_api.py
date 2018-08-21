from rest_framework.views import APIView
from onorapp.models import Users
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from onorapp.Serializers.loginserializer import LoginSerializers
from django.core import serializers

class login(APIView):
    def post(self,request,format=None):
        print(request.data)
        emailId=request.data['emailId']
        password=request.data['password']
        #print("email password: ",emailid,password)
        if (User.objects.filter(emailId=emailId).exists()):
            user = authenticate(emailId=emailId, password = password)
            login(request,user)
            return JsonResponse({"message":"success"})
        else:
            return JsonResponse({"message":'Looks like a username with that email or password already exists'})
