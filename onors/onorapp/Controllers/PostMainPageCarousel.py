from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from django.core import serializers
from onorapp.models import MainPageCarousel
from onorapp.Serializers.MainPageCarouselSerializer import MainPageCarouselSerializers
from django.http import Http404
from rest_framework import status
from django.http import JsonResponse

class addMainPageCarousel(APIView):
    def get(self,request,*args,**kwargs):
        try:
            get=MainPageCarousel.objects.all()
            serializer=MainPageCarouselSerializers(get,many=True)
            return Response(serializer.data)
        except MainPageCarousel.DoesNotExist:
            raise Http404

    def post(self,request,format=None):
        try:
            serializer=MainPageCarouselSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=301)
        except Http404:
            return JsonResponse({"message":"data not added"})
