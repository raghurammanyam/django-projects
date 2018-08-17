from django.core import serializers
from Catalog.models import Users
from Catalog.serializers.UserSerializers import UsersSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
import crypt
from Catalog.Controllers.send_mail_controller import SendMail;




class CreateUser(APIView):
    def get(self, request,*args,**kwargs):
        user = Users.objects.all()
        serializer = UsersSerializer(user, many=True)
        return JsonResponse({'Users Data':serializer.data})

    def post(self, request, format=None,*args,**kwargs):
      print("posting data:",request.data)
      role=request.data['role']
      First_name = request.data['First_name']
      Last_name = request.data['Last_name']
      Password = crypt.crypt(request.data['Password'])
      print("password:",Password)
      Mobile_no = request.data['Mobile_no']
      Email = request.data['Email']
      Address = request.data['Address']
      status = request.data['status']
      user = {'role':role,'First_name':First_name,'Last_name':Last_name,'Address':Address,'Password': Password,'Email':Email,'Mobile_no':Mobile_no,'status':status}
      print("dictonary:",user)
      serializer = UsersSerializer(data=user)
      if serializer.is_valid():
          serializer.save()
          mail_id = serializer['Email']
          mail = SendMail.send(mail_id)
          if(mail == 'success'):
		return JsonResponse({"message":successfully sent})          
          print("address:",mail_id)

          return JsonResponse({'create user':serializer.data})
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
