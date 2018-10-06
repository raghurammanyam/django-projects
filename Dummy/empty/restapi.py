from django.shortcuts import render
from rest_framework.response import Response
from django.core.files.storage import default_storage
from rest_framework.views import APIView
from django.core.files.base import ContentFile
from django.http import JsonResponse
from django.core import serializers
from .serializer import userSerializer
from django.core.mail import send_mail
from django.utils.log import AdminEmailHandler
from django.core.mail.message import EmailMultiAlternatives
from django.conf import settings
import base64
from django.db import  DatabaseError
from empty.db import database
from Dummy.settings import *



import logging
logger = logging.getLogger('empty.restapi')
class createuser(APIView):

    def post(self, request):
            import logging
            logger = logging.getLogger('empty.restapi')

            try:
               serializer =userSerializer(data=request.data)
               if serializer.is_valid():
                   serializer.save()
                   return JsonResponse({"data":serializer.data})
               a=logger.error(serializer.errors)
               print (a)
               TEXT = ("error log message:",logger)
               message = """From: %s\nTo: %s\n\n%s
               """% (DEFAULT_FROM_EMAIL, ", ".join(ADMINS),TEXT)
               error = logger.makeRecord(logger.name,logging.error(serializer.errors),0, 0,u"Subject: Some error occured",None, None, "", None,).split(',', maxsplit=1)
               #MyEmailHandler.emit()
               error.email_body = logger.error(serializer.errors)
               #MyEmailHandler.emit(record)

              # logger.handle(error)
                           #message = ''.join(message.splitlines())
               send_mail('you got an error',error, DEFAULT_FROM_EMAIL,ADMINS,fail_silently=True)
            except DatabaseError as e:
                 logger.debug( DatabaseError)
