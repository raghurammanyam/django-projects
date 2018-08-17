from django.core import serializers
from Catalog.models import MainPage
from Catalog.serializers.mainpageSerializer import MainPageSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class getUpdateDeleteMainpage(APIView):
    def get_object(self, id):
        try:
            return MainPage.objects.get(id=id)
        except :
            raise Http404

    def get(self, request, id, format=None):
        try:
            mainpage = self.get_object(id)
            serializer = MainPageSerializer(mainpage)
            return Response(serializer.data)
        except Http404:
            return JsonResponse({"message:":"MainPage not found"})
    def put(self, request, id, format=None):
        try:
            mainpage = self.get_object(id)
            serializer = MainPageSerializer(mainpage, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except :
            return JsonResponse({"message:":"Mainpage not updated"})

    def delete(self, request, id, format=None):
        try:
            mainpage = self.get_object(id)
            mainpage.delete()
            return JsonResponse({"message:":"Main page  deleted"})
        except :
            return JsonResponse({"message:":"Main page not deleted"})
