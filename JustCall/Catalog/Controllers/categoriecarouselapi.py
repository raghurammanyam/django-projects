from django.core import serializers
from Catalog.models import categorie_curosels
from Catalog.serializers.CategoriecuroselsSerilizer import categorie_curoselsSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response




class CreateCategoriecarusel(APIView):
    def get(self, request,*args,**kwargs):
        carousel = categorie_curosels.objects.all()
        serializer = categorie_curoselsSerializer(carousel, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = categorie_curoselsSerializer(data=request.data)
        print (serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
