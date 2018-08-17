from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from django.core import serializers
from django.http import JsonResponse
from onorapp.models import Roles
from onorapp.Serializers.RolesSerializer import RolesSerializers
from django.http import Http404
from rest_framework import status

class addRoles(APIView):
    def get(self,request,*args,**kwargs):
        try:
            get=Roles.objects.all()
            serializer=RolesSerializers(get,many=True)
            return Response(serializer.data)
        except Roles.DoesNotExist:
            raise Http404

    def post(self,request,format=None):
        try:
            serializer=RolesSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=301)
        except Http404:
            return JsonResponse({"message":"data not added"})
