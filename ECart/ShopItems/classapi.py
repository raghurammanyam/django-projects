from .models import Customers,Items,categories,Orders
from  django.core import serializers
from .serializers import CustomersSerializer,categoriesSerializer,ItemsSerializer,OrdersSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import Http404,JsonResponse


class List(APIView):
    def get(request,*args,**kwargs):
        cus = Customers.objects.all()
        print(cus)
        data = CustomersSerializer(cus,many=True).data
        return Response(data)

class Bull(APIView):
    """
    List
    """
    def get(self, request,*args,**kwargs):
        snippets = Customers.objects.all()
        serializer = CustomersSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CustomersSerializer(data=request.data)
        print (serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Detail(APIView):
    def get_object(self, id):
        try:
            return Customers.objects.get(id=id)
        except customer.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        cust = self.get_object(id)
        serializer = CustomersSerializer(cust)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        cust = self.get_object(id)
        serializer = customersSerializer(cust, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        cust = self.get_object(id)
        cust.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Rossum(APIView):
    def get_object(self, id):
        try:
            return Customers.objects.get(id=id)
        except :
            raise Http404

    def get(self, request, id, format=None):
        try:
            cust = self.get_object(id)
            serializer = CustomersSerializer(cust)
            return Response(serializer.data)
        except Http404:
            return JsonResponse({"message:":"customer not found"})
    def put(self, request, id, format=None):
        try:
            cust = self.get_object(id)
            serializer = customersSerializer(cust, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except :
            return JsonResponse({"message:":"customer not updated"})

    def delete(self, request, id, format=None):
        try:
            cust = self.get_object(id)
            cust.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except :
            return JsonResponse({"message:":"customer not deleted"})


class Van(APIView):
    def get_object(self, id):
        try:
            return categories.objects.get(id=id)
        except :
            raise Http404
    def get(self, request, id, format=None):
        try:
            cate = self.get_object(id)
            serializer = categoriesSerializer(cate)
            return Response(serializer.data)
        except Http404:
            return JsonResponse({"message:":"CATEGORIE not found"})

    def put(self, request, id, format=None):
        try:
            cate = self.get_object(id)
            serializer = categoriesSerializer(cate, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except :
            return JsonResponse({"message:":"categorie not updated"})
    def delete(self, request, id, format=None):
        try:
            cate = self.get_object(id)
            cate.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except :
            return JsonResponse({"message:":"CATEGORIE not deleted"})


class Dell(APIView):
    def get_object(self,id):
        try:
            return Items.objects.get(id=id)
        except :
            raise Http404
    def get(self, request, id, format=None):
        try:
            cate = self.get_object(id)
            serializer = ItemsSerializer(cate)
            return Response(serializer.data)
        except Http404:
            return JsonResponse({"message:":"Items not found"})

    def put(self, request, id, format=None):
        try:
            cate = self.get_object(id)
            serializer = ItemsSerializer(cate, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except :
            return JsonResponse({"message:":"ITEM not updated"})
    def delete(self, request, id, format=None):
        try:
            cate = self.get_object(id)
            cate.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except :
            return JsonResponse({"message:":"ITEM not deleted"})

class Key(APIView):
    def get_object(self, id):
        try:
            return Orders.objects.get(id=id)
        except :
            raise Http404
    def get(self, request, id, format=None):
        try:
            cate = self.get_object(id)
            serializer = OrdersSerializer(cate)
            return Response(serializer.data)
        except Http404:
            return JsonResponse({"message:":"Orders not found"})

    def put(self, request, id, format=None):
        try:
            cate = self.get_object(id)
            serializer = OrdersSerializer(cate, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except :
            return JsonResponse({"message:":"Orders not updated"})
    def delete(self, request, id, format=None):
        try:
            cate = self.get_object(id)
            cate.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except :
            return JsonResponse({"message:":"orders not deleted"})


class Pad(APIView):
    """
    List
    """
    def get(self, request,*args,**kwargs):
        try:
            snippets = Customers.objects.all()
            serializer = CustomersSerializer(snippets, many=True)
            return Response(serializer.data)
        except:
            return JsonResponse({"message:":"customer not found"})

    def post(self, request, format=None):
        try:
                serializer = CustomersSerializer(data=request.data)
                print (serializer)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return JsonResponse({"message:":" not found"})
