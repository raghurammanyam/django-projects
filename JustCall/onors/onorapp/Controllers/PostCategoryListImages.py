from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from django.core import serializers
from onorapp.models import CategoryListImages
from onorapp.Serializers.CategoryListimagesSerializer import CategoryListImageSerializers,GetCategoryListImageSerializers
from django.http import Http404
from django.http import JsonResponse
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.settings import api_settings
from rest_framework.pagination import PageNumberPagination
from onorapp.Controllers.pagination import StandardResultsSetPagination

class createItemImages(APIView):
    def get(self,request,*args,**kwargs):
        try:
            print(request.META.get('HTTP_PAGES'))
            n = request.META.get('HTTP_PAGES')
            get=CategoryListImages.objects.all()#[:api_settings.PAGE_SIZE]

            paginator = Paginator(get, n)
            a=paginator.page(1)
            s=paginator.page(1).next_page_number()
            print("pagedata:",s)
            b=paginator.page(paginator.num_pages)
            serializer=GetCategoryListImageSerializers(a,many=True,context={'request': self.request})
            #return paginator.get_paginated_response(serializer.data).data"""
            #return Response(request.META)
            return JsonResponse({"success":True,"data":serializer.data})
        except CategoryListImages.DoesNotExist:
            raise Http404

    def post(self,request,format=None):
        try:
            serializer=CategoryListImageSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"success":True,"data":serializer.data})

        except Http404:
            return JsonResponse({"success":False,"message":"ItemImages data not added"})

class Images(APIView):
    def get(self,request,*args,**kwargs):
        try:
            print(request.META.get('HTTP_PAGES'))
            n = request.META.get('HTTP_PAGES')
            get=CategoryListImages.objects.all()#[:api_settings.PAGE_SIZE]
            paginator = StandardResultsSetPagination()                  
            paginator.page_size = n
            sun=paginator.paginate_queryset(get,request )
            print(sun)

            #paginator = Paginator(get, n)
            #a=paginator.page(1)
            #s=paginator.page(1).next_page_number()
            #print("pagedata:",s)
            #b=paginator.page(paginator.num_pages)
            serializer=GetCategoryListImageSerializers(sun,many=True,context={'request': self.request})
            #return paginator.get_paginated_response(serializer.data).data"""
            #return Response(request.META)
            return paginator.get_paginated_response(serializer.data)
            #return JsonResponse({"success":True,"data":serializer.data})
        except CategoryListImages.DoesNotExist:
            raise Http404
