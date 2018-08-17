from django.core import serializers
from Catalog.models import Categories
from Catalog.serializers.CategorieSerializer import CategoriesSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class getUpdateDeleteCategorie(APIView):
    def get_object(self, id):
        try:
            return Categories.objects.get(id=id)
        except :
            raise Http404

    def get(self, request, id, format=None):
        try:
            cat = self.get_object(id)
            serializer = CategoriesSerializer(cat)
            return Response(serializer.data)
        except Http404:
            return JsonResponse({"message:":"categorie not found"})
    def put(self, request, id, format=None):
        try:
            categorie = self.get_object(id)
            serializer = CategoriesSerializer(categorie, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except :
            return JsonResponse({"message:":"categorie not updated"})

    def delete(self, request, id, format=None):
        try:
            categorie = self.get_object(id)
            categorie.delete()
            return JsonResponse({"message:":"categorie  deleted"})
        except :
            return JsonResponse({"message:":"categorie not deleted"})
