from django.shortcuts import render
from rest_framework.response import Response
from django.core.files.storage import default_storage
from rest_framework.views import APIView
from django.core.files.base import ContentFile
from django.http import JsonResponse
import base64
from django.db import  DatabaseError
from empty.db import database
import logging
logger = logging.getLogger('empty.views')
class Bot(APIView):

    def post(self, request, format=None):

            try:
                data=request.FILES['images']

                path = default_storage.save('heart_of_the_swarm.xls', ContentFile(data.read()))
                a=database(path)
                logger.debug('something went wrong')
                return Response(a)
            except DatabaseError as e:
                 logger.debug( DatabaseError)



# Create your views here.
