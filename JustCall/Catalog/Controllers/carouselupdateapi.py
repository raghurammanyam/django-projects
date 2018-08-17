from django.core import serializers
from Catalog.models import Carousels
from Catalog.serializers.CarouselSerializers import CarouselsSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

class getUpdateDeleteCarousel(APIView):
    def get_object(self, id):
        try:
            return Carousels.objects.get(id=id)
        except :
            raise Http404

    def get(self, request, id, format=None):
        try:
            carusel = self.get_object(id)
            serializer = CarouselsSerializer(carusel)
            return Response(serializer.data)
        except Http404:
            return JsonResponse({"message:":"carusel not found"})
    def put(self, request, id, format=None):
        try:
            carusel = self.get_object(id)
            serializer = CarouselsSerializer(carusel, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except :
            return JsonResponse({"message:":"carusel not updated"})

    def delete(self, request, id, format=None):
        try:
            carusel = self.get_object(id)
            carusel.delete()
            return JsonResponse({"message:":"carusel  deleted"})
        except :
            return JsonResponse({"message:":"carusel not deleted"})
