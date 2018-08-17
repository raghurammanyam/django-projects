from django.core import serializers
from Catalog.models import Item_Pics
from Catalog.serializers.listpicsserializer import Item_PicsSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response



class CreateItemPic(APIView):
    def get(self, request,*args,**kwargs):
        pic = Item_Pics.objects.all()
        serializer = Item_PicsSerializer(pic, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Item_PicsSerializer(data=request.data)
        print (serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
