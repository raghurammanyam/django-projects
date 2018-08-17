from collections import Counter
from  django.core import serializers
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import Http404,JsonResponse
from .models import Inventory,Bill
from .serializers import InventorySerializer,BillSerializer
from django.db.models import F
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict




class Bot(APIView):
    def get(self, request,*args,**kwargs):
        try:
            get = Inventory.objects.all()
            serializer = InventorySerializer(get,many=True)
            return Response(serializer.data)
        except Inventory.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        serializer = InventorySerializer(data=request.data)
        print (serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update(request,id):
    print(request.data)
    a=Inventory.objects.filter(id=id).first()
    #b = dict([obj.as_dict() for obj in a])
    b=model_to_dict(a)
    print(b)
    z=dict(Counter(b)+Counter(request.data))
    print(z)
    #.update(z)
    serializer =InventorySerializer(a,data=z)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status= 301)


class like(APIView):
    def get(self, request,*args,**kwargs):
        try:
            get = Bill.objects.all()
            serializer = BillSerializer(get,many=True)
            return Response(serializer.data)
        except Inventory.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        serializer = BillSerializer(data=request.data)
        print(request.data)
        print("-------------------------------------------")
        a=Inventory.objects.filter(id=1).first()
        b=model_to_dict(a)
        print(b)
        print("----------------------------------------------")
        v=dict(Counter(b)-Counter(request.data))
        print(v)
        x =InventorySerializer(a,data=v)
        if x.is_valid():
            x.save()
        print (serializer)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
