
from django.http import JsonResponse
from rest_framework.response import Response
from django.core import serializers
from .serializers import CustomersSerializer,categoriesSerializer,ItemsSerializer,OrdersSerializer
from .models import Customers,categories,Items,Orders
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['POST'])
def post(request):
    mob = categoriesSerializer(data=request.data)
    if mob.is_valid():
        mob.save()
        return Response(mob.data,status=301)



@api_view(['POST'])
def cust(request):
    user = CustomersSerializer(data=request.data)
    if user.is_valid():
        user.save()
        return Response(user.data,status=301)



@api_view(['POST'])
def pro(request):
    serializer = ItemsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=301)

@api_view(['POST'])
def ord(request):
    serializer = OrdersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status =301)

@api_view(['GET'])
def get(request,_id):
    dat = Customers.objects.filter(id=_id)
    if dat:
        serializer = CustomersSerializer(dat,many=True)
        return Response(serializer.data)


@api_view(['GET'])
def cat(request,_id):
    dat = categories.objects.filter(id=_id)
    if dat:
        serializer = categoriesSerializer(dat,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def apt(request):
    dat = Items.objects.all()
    if dat:
        serializer = ItemsSerializer(dat,many=True)
        return Response(serializer.data)


@api_view(['GET'])
def call(request,_id):
    dat = Orders.objects.filter(id=_id)
    if dat:
        serializer = OrdersSerializer(dat,many=True)
        return Response(serializer.data)


@api_view(['PUT'])
def put(request,_name):
     serializer = CustomersSerializer(Customers,data=request.POST.get('name'),context={'request':request})
     print (serializer)
     if serializer.is_valid():
         return Response(serializer.data)

            #serializer.save()

     #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







    #"""print(request.data)
    #cust = Customers.objects.filter(name=request.data['name'])
    #cust.update(name=request.data["name"])
    #serializer = CustomersSerializer(data=cust, many=True)
    #if serializer.is_valid():
    #    serializer.save()
    #    return Response(serializer.data, status= 301)"""



@api_view(['PUT'])
def update(request,_name):
    print(request.data)
    cust = categories.objects.filter(name=request.data['name'])
    cust.update(name=request.data["name"])
    serializer = categoriesSerializer(data=cust, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status= 301)



@api_view(['PUT'])
def oak(request,_name):
    print(request.data)
    cust = Items.objects.filter(name=request.data['name'])
    cust.update(name=request.data["name"])
    serializer = ItemsSerializer(data=cust, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status= 301)


@api_view(['PUT'])
def tes(request,_id):
    print(request.data)
    cust = Orders.objects.filter(id=request.data['id'])
    cust.update(id=request.data["id"])
    serializer = OrdersSerializer(data=cust, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status= 301)
@api_view(['DELETE'])
def dele(request,_id):
    Customers.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)




    """ mul = Customers.objects.filter(id=_id)
     mul.delete()
     serializer = CustomersSerializer(data=mul, many=True)
     if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status= 301)"""


@api_view(['DELETE'])
def sat(request,_id):
     mul = categories.objects.filter(id=_id)
     mul.delete()
     serializer = categoriesSerializer(data=mul, many=True)
     if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status= 301)

@api_view(['DELETE'])
def gan(request,_id):
     mul = Items.objects.filter(id=_id)
     mul.delete()
     serializer = ItemsSerializer(data=mul, many=True)
     if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status= 301)

@api_view(['DELETE'])
def bas(request,_id):
     mul = Orders.objects.filter(id=_id)
     mul.delete()
     serializer = OrdersSerializer(data=mul, many=True)
     if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status= 301)
