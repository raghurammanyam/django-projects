from django.shortcuts import render
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from django.core import serializers
from .serializer import sportsSerializer,playerSerializer
from django.http import JsonResponse
from .models import sports,player
from django.http import Http404
from rest_framework import status

class sport(APIView):
    def get(self,request,*args,**kwargs):
        try:
            get=sports.objects.all()
            serializer=sportsSerializer(get,many=True)
            print("sports:",serializer)
            return JsonResponse({"context":serializer.data})
        except sports.DoesNotExist:
            raise Http404

class getplayer(APIView):
    def get(self,request,*args,**kwargs):
        ge=player.objects.all()
        serializer=playerSerializer(ge,many=True)
        return JsonResponse({"context":serializer.data})





# Create your views here.
