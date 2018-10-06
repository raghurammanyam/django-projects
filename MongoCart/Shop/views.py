from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import render
from django.core import serializers
from rest_framework.views import APIView
from .serializers import CustomersModelSerializer,CategoriesModelSerializer,ItemsModelSerializer,OrdersModelSerializer
from .models import CustomersModel,CategoriesModel,ItemsModel,OrdersModel
from django.http import JsonResponse,Http404
from rest_framework import status
from mongoengine import *
connect('Shop')

class Pad(APIView):
    """
    List
    """
    def get(self, request,*args,**kwargs):
        try:
            cust = OrdersModel.objects.all()
            serializer = OrdersModelSerializer(cust, many=True)
            return Response(serializer.data)
        except:
            return JsonResponse({"message:":"order not found"})

    def post(self, request, format=None):
        try:
                serializer = OrdersModelSerializer(data=request.data)
                print (serializer)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return JsonResponse({"message:":" not found"})

class Details(APIView):
     def get_object(self,status):
         try:
             return OrdersModel.objects.get(status=status)
         except     OrdersModel.DoesNotExist:
             raise Http404

     def get(self, request, status, format=None):
         try:
             use= self.get_object(status=status)
             serializer= OrdersModelSerializer(use)
             return Response(serializer.data)
         except Http404:
             return Response(" Order NOT Found")

     def post(self, request, format=None):
         try:
             serializer = OrdersModelSerializer(data=request.data)
             if serializer.is_valid():
                 serializer.save()
                 return Response(serializer.data, status=status.HTTP_201_CREATED)
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
         except Http404:
             return Response(" Order NOT POSTED")





# Create your views here.
