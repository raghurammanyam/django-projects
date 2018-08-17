from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from django.core import serializers
from onorapp.models import CategoryList
from onorapp.Serializers.CategoryListSerializer import CategoryListSerializers
from django.http import JsonResponse
from django.http import Http404
from rest_framework import status

class addCategoryList(APIView):
    def get(self,request,*args,**kwargs):
        try:
            get=CategoryList.objects.all()
            serializer=CategoryListSerializers(get,many=True)
            return Response(serializer.data)
        except CategoryList.DoesNotExist:
            raise Http404

    def post(self,request,format=None):
        try:
            serializer=CategoryListSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=301)
        except Http404:
            return JsonResponse({"message:":"listings not found"})
