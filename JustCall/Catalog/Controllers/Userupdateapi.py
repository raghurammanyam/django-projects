from django.core import serializers
from Catalog.models import Users
from Catalog.serializers.UserSerializers import UsersSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
import crypt



class getUpdateDeleteUser(APIView):
    def get_object(self, id):
        try:
            return Users.objects.get(id=id)
        except :
            raise Http404

    def get(self, request, id, format=None):
        try:
            user = self.get_object(id)
            serializer = UsersSerializer(user)
            return JsonResponse({'user data':serializer.data})
        except Http404:
            return JsonResponse({"message:":"customer not found"})
    def put(self, request, id, format=None):
        try:
            user = self.get_object(id)
            print("updating data:",request.data)
            id=request.data['id']
            role=request.data['role']
            First_name = request.data['First_name']
            Last_name = request.data['Last_name']
            Password = crypt.crypt(request.data['Password'])
            print("password:",Password)
            Mobile_no = request.data['Mobile_no']
            Email = request.data['Email']
            Address = request.data['Address']
            status = request.data['status']
            ram = {'id':id,'role':role,'First_name':First_name,'Last_name':Last_name,'Address':Address,'Password': Password,'Email':Email,'Mobile_no':Mobile_no,'status':status}
            serializer = UsersSerializer(user,data=ram)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'user update data':serializer.data})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except :
            return JsonResponse({"message:":"customer not updated"})

    def delete(self, request, id, format=None):
        try:
            user = self.get_object(id)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except :
            return JsonResponse({"message:":"customer not deleted"})
