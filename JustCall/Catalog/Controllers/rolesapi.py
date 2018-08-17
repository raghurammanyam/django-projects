from django.core import serializers
from Catalog.models import Roles
from Catalog.serializers.RoleSerializer import RolesSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class CreateRoles(APIView):
    def get(self, request,*args,**kwargs):
        role = Roles.objects.all()
        serializer = RolesSerializer(role, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RolesSerializer(data=request.data)
        print (serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
