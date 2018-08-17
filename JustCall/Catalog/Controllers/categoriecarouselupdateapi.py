from django.core import serializers
from Catalog.models import categorie_curosels
from Catalog.serializers.CategoriecuroselsSerilizer import categorie_curoselsSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response



class getUpdateDeleteCategorieCarousel(APIView):
    def get_object(self, id):
        try:
            return categorie_curosels.objects.get(id=id)
        except :
            raise Http404

    def get(self, request, id, format=None):
        try:
            carusel = self.get_object(id)
            serializer = categorie_curoselsSerializer(carusel)
            return Response(serializer.data)
        except Http404:
            return JsonResponse({"message:":"categorie carusel not found"})
    def put(self, request, id, format=None):
        try:
            carusel = self.get_object(id)
            serializer = categorie_curoselsSerializer(carusel, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except :
            return JsonResponse({"message:":"categoriecarusel not updated"})

    def delete(self, request, id, format=None):
        try:
            carusel = self.get_object(id)
            carusel.delete()
            return JsonResponse({"message:":"categoriecarusel  deleted"})
        except :
            return JsonResponse({"message:":"categoriecarusel not deleted"})
