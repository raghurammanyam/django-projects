from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from django.core import serializers
from django.http import JsonResponse
from onorapp.models import Users
from onorapp.Serializers.UserSerializer import UserSerializers,UserroleSerializers
from django.http import Http404
from rest_framework import status
import crypt

class getUpdateDeleteUsers(APIView):
    def get_object(self,id):
        try:
            return Users.objects.get(id=id)
        except:
            raise Http404

    def get(self, request, id, format=None):
        try:
            get=self.get_object(id)
            serializer=UserroleSerializers(get)
            return JsonResponse({"success":True,"data":serializer.data})
        except Http404:
            return JsonResponse({"success":False,"message:":"Users not found"})

    def put(self,request,id,format=None):
        try:
            obj=self.get_object(id)
            password=crypt.crypt(request.data['password'])
            user={'password':password}
            serializer=UserSerializers(obj,data=user,partial=True)
            if serializer.is_valid():
                if(serializer.validated_data['password']):
                    serializer.save()
                    return Response({"success":True,"data":serializer.data})
        except:
            obj=self.get_object(id)
            serializer=UserSerializers(obj,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"success":True,"data":serializer.data})

    def delete(self,request,id,format=None):
        try:
            obj=self.get_object(id)
            obj.delete()
            return Response({"success":True,"message":"Users data  deleted"})
        except Http404:
            return JsonResponse({"success":False,"message":"Users data not deleted"})
