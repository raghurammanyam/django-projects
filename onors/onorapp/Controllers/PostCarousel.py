from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from django.core import serializers
from onorapp.Serializers.CarouselSerializer import CarouselSerializers
from django.http import JsonResponse
from onorapp.models import Carousel
from django.http import Http404
from rest_framework import status

class addCarousel(APIView):
    def get(self,request,*args,**kwargs):
        try:
            get=Carousel.objects.all()
            serializer=CarouselSerializers(get,many=True)
            return Response(serializer.data)
        except Carousel.DoesNotExist:
            raise Http404
    def post(self,request,format=None):
        try:
            serializer=CarouselSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=301)
        except Http404:
            return Response({"message":"data not added"})
