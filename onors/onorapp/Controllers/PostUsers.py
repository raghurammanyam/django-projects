from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from django.core import serializers
from django.http import JsonResponse
from onorapp.models import Users
from onorapp.Serializers.UserSerializer import UserSerializers
from django.http import Http404
from rest_framework import status
import crypt
from onorapp.Controllers.send_mail_controller import SendMail

class addUsers(APIView):
    def get(self,request,*args,**kwargs):
        try:
            get=Users.objects.all()
            serializer=UserSerializers(get,many=True)
            return Response(serializer.data)
        except Users.DoesNotExist:
            raise Http404

    def post(self,request,format=None):
        try:
            serializer=UserSerializers(data=request.data)
            role = request.data['role']
            first_name = request.data['first_name']
            last_name = request.data['last_name']
            mobile_no = request.data['mobile_no']
            address =  request.data['address']
            emailId = request.data['emailId']
            password = crypt.crypt(request.data['password'])
            status = request.data['status']
            users={"role":role,"first_name":first_name,"last_name":last_name,"mobile_no":mobile_no,"address":address,"emailId":emailId,"password":password,"status":status}
            serializer=UserSerializers(data=users)
            if serializer.is_valid():
                serializer.save()
                mail_id = request.data['emailId']
                mail = SendMail.send(mail_id)
                if(mail == 'success'):
                     return JsonResponse({"message":"successfully sent"})                      
                return Response(serializer.data,status=301)
        except Http404:
            return JsonResponse({"message":"data not added"})
