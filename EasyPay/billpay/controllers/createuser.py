from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers
from django.http import JsonResponse
from billpay.models import users
from billpay.serializers.userserializer import userSerializer
from django.http import Http404
from rest_framework import status
from django.conf import settings
import logging
logger = logging.getLogger('billpay.createuser')
class addUsers(APIView):
    def get(self,request,*args,**kwargs):
        try:
            get=users.objects.all()
            serializer=userSerializer(get,many=True)
            return JsonResponse({"success":True,"data":serializer.data})
        except users.DoesNotExist:
            raise Http404

    def post(self,request,format=None):
        try:
            serializer=userSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                logger.info(serializer.data)
                return JsonResponse({'data':serializer.data,'message':'user added suceesfully'})
            logger.error(serializer.errors)                    #return Response(serializer.data,status=301)
            return JsonResponse({"message":serializer.errors})
        except Http404:
            return JsonResponse({"success":False,"message":"data not added"})
