from django.core import serializers
from Catalog.models import Item_Pics
from Catalog.serializers.listpicsserializer import Item_PicsSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class getUpdateDeleteItemPic(APIView):
    def get_object(self, id):
        try:
            return Item_Pics.objects.get(id=id)
        except :
            raise Http404

    def get(self, request, id, format=None):
        try:
            pic = self.get_object(id)
            serializer = Item_PicsSerializer(pic)
            return Response(serializer.data)
        except Http404:
            return JsonResponse({"message:":"list pic not found"})
    def put(self, request, id, format=None):
        try:
            pic = self.get_object(id)
            serializer = Item_PicsSerializer(pic, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except :
            return JsonResponse({"message:":"list pic not updated"})

    def delete(self, request, id, format=None):
        try:
            pic = self.get_object(id)
            pic.delete()
            return JsonResponse({"message:":"list pic  deleted"})
        except :
            return JsonResponse({"message:":"list pic not deleted"})
