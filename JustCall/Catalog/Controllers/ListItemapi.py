from django.core import serializers
from Catalog.models import List_Of_Items
from Catalog.serializers.ListSerializer import List_Of_ItemsSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response



class CreateItem(APIView):
    def get(self, request,*args,**kwargs):
        list = List_Of_Items.objects.all()
        serializer = List_Of_ItemsSerializer(list, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = List_Of_ItemsSerializer(data=request.data)
        print (serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
