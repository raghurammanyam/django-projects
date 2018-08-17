from django.core import serializers
from Catalog.models import List_Of_Items
from Catalog.serializers.ListSerializer import List_Of_ItemsSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class getUpdateDeleteItem(APIView):
    def get_object(self, id):
        try:
            return List_Of_Items.objects.get(id=id)
        except :
            raise Http404

    def get(self, request, id, format=None):
        try:
            item = self.get_object(id)
            serializer = List_Of_ItemsSerializer(item)
            return Response(serializer.data)
        except Http404:
            return JsonResponse({"message:":"item not found"})
    def put(self, request, id, format=None):
        try:
            item = self.get_object(id)
            serializer = List_Of_ItemsSerializer(item, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except :
            return JsonResponse({"message:":"item not updated"})

    def delete(self, request, id, format=None):
        try:
            item = self.get_object(id)
            item.delete()
            return JsonResponse({"message:":"item  deleted"})
        except :
            return JsonResponse({"message:":"item not deleted"})
