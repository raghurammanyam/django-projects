from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from django.core import serializers
from django.http import JsonResponse
from onorapp.models import Users
from onorapp.Serializers.UserSerializer import UserSerializers
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
            serializer=UserSerializers(get)
            return Response(serializer.data)
        except Http404:
            return JsonResponse({"message:":"listings not found"})

    def put(self,request,id,format=None):
        try:
            obj=self.get_object(id)
            role = request.data['role']
            first_name = request.data['first_name']
            last_name = request.data['last_name']
            mobile_no = request.data['mobile_no']
            address =  request.data['address']
            emailId = request.data['emailId']
            password = crypt.crypt(request.data['password'])
            status = request.data['status']
            users={"role":role,"first_name":first_name,"last_name":last_name,"mobile_no":mobile_no,"address":address,"emailId":emailId,"password":password,"status":status}
            serializer=UserSerializers(obj,data=users)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
        except Http404:
            return JsonResponse({"message":"data not updated"})

    def delete(self,request,id,format=None):
        try:
            obj=self.get_object(id)
            obj.delete()
            return Response({"message":"data  deleted"})
        except Http404:
            return JsonResponse({"message":"data not deleted"})
