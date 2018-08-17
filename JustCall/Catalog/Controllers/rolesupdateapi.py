from django.core import serializers
from Catalog.models import Roles
from Catalog.serializers.RoleSerializer import RolesSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class getUpdateRole(APIView):
    def get_object(self, id):
        try:
            return Roles.objects.get(id=id)
        except :
            raise Http404

    def get(self, request, id, format=None):
        try:
            role = self.get_object(id)
            serializer = RolesSerializer(role)
            return Response(serializer.data)
        except Http404:
            return JsonResponse({"message:":"role not found"})
    def put(self, request, id, format=None):
        try:
            role= self.get_object(id)
            serializer = RolesSerializer(role, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except :
            return JsonResponse({"message:":"Role not updated"})
