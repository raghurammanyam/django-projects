from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers
from django.http import JsonResponse
from billpay.models import transactions
from billpay.serializers.transactionserializer import transactionSerializer,gettransactionSerializer
from django.http import Http404
from rest_framework import status
from django.conf import settings
import logging
logger = logging.getLogger('billpay.transaction')

class addtransaction(APIView):
    def get(self,request,*args,**kwargs):
        try:
            get=transactions.objects.all()
            serializer=gettransactionSerializer(get,many=True)
            return JsonResponse({"success":True,"data":serializer.data})
        except transactions.DoesNotExist:
            raise Http404

    def post(self,request,format=None):
        try:
            serializer=transactionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                logger.info(serializer.data)
                return JsonResponse({'data':serializer.data,'message':'transaction added suceesfully'})
            logger.error(serializer.errors)
            return JsonResponse({"message":serializer.errors})
        except Http404:
            return JsonResponse({"success":False,"message":"transaction not added"})
