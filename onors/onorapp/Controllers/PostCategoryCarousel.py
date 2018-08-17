from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from django.core import serializers
from onorapp.models import CategoryCarousel
from onorapp.Serializers.CategoryCarouselSerializer import CategoryCarouselSerializers
from django.http import JsonResponse
from django.http import Http404
from rest_framework import status

class addCategoryCarousel(APIView):
    def get(self,request,*args,**kwargs):
        try:
            get=CategoryCarousel.objects.all()
            serializer=CategoryCarouselSerializers(get,many=True)
            return Response(serializer.data)
        except CategoryCarousel.DoesNotExist:
            raise Http404

    def post(self,request,format=None):
        try:
            serializer=CategoryCarouselSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=301)
        except Http404:
            return JsonResponse({"message":"data not added"})
