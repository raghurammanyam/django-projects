from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers
from django.http import JsonResponse
from billpay.models import payments,transactions,user_credits
from billpay.serializers.paymentserializer import paymentSerializer
from billpay.serializers.transactionserializer import transactionSerializer
from billpay.serializers.creditserializer import creditSerializer
from django.http import Http404
from rest_framework import status
from django.forms.models import model_to_dict
import decimal
from django.db import transaction
from django.conf import settings
from django.db import connection
from django.db.models import F
import logging
logger = logging.getLogger('billpay.pay')
pay_logger = logging.getLogger('billpay.payments')
trans_logger =logging.getLogger('billpay.transaction')
credit_logger=logging.getLogger('billpay.credit')


class addpayment(APIView):
    def get(self,request,*args,**kwargs):
        try:
            get=users.objects.all()
            serializer=paymentSerializer(get,many=True)
            return JsonResponse({"success":True,"data":serializer.data})
        except users.DoesNotExist:
            raise Http404

    def post(self,request,format=None):
        try:
            serializer=paymentSerializer(data=request.data)
            if serializer.is_valid():
                transaction = serializer.data['transaction']
                trans = transactions.objects.filter(id=transaction,status=upaid).first()
                h=model_to_dict(trans)
                k=h['amount']
                print('total:',h['amount'])
                payment_amount = serializer.data['payment_amount']
                user=serializer.data['user']
                print("amount:",payment_amount)
                pay_via = serializer.data['pay_via']
                pay_status = serializer.data['pay_status']
                partial_amount = k-decimal.Decimal(payment_amount)
                pay = ({"transaction":transaction,"payment_amount":payment_amount,"user":user, "pay_via":pay_via, "partial_amount":partial_amount,"pay_status":pay_status})
                serializer=paymentSerializer(data=pay)
                if partial_amount>0:
                    a={'partial_status':True}
                    bill=transactionSerializer(trans,data=a,partial=True)
                    logger.info(bill.data)
                else:
                    v={'status':'paid','partial_status':False}
                    bill= transactionSerializer(trans,data=v,partial=True)
                    logger.info(bill.data)

                if bill.is_valid():
                    bill.save()
                    if serializer.is_valid():
                        serializer.save()
                        pay_logger.info(serializer.data)
                        return JsonResponse({'data':serializer.data,'message':'payment added suceesfully'})
                    pay_logger.error(serializer.errors)
                    return JsonResponse({"message":serializer.errors})

        except Http404:
            return JsonResponse({"success":False,"message":"payment not added"})


class updatebill(APIView):
     def post(self,request):
         try:
             serializer=paymentSerializer(data=request.data)
             print('ffff',serializer)
             if serializer.is_valid():
                 user = serializer.data['user']
                 pay_via = serializer.data['pay_via']
                 pay_status = serializer.data['pay_status']
                 print('zzzz',user)
                 bill = (transactions.objects.filter(user=user,status='not_paid'))
                 ser=transactionSerializer(bill,many=True)
                 id_amount={}
                 id=[]
                 y=[]
                 s=[]
                 for a in bill:
                     dit={int(a.id):int(a.amount)}
                     id_amount.update(dit)
                 print("id's with amount",id_amount)
                 su = sum(id_amount[item] for item in id_amount)
                 payment_amount = serializer.data['payment_amount']
                 pay_amount = payment_amount
                 for key,values in id_amount.items():
                     if float(pay_amount)>=values:
                         pay_amount = float(pay_amount)-values
                         id.append(key)
                         y.append(pay_amount)
                         print(key,pay_amount,values)
                     else:
                         s.append(key)
                 print("guhdh:",y)
                 print("yt:",s)
                 print("f: ",payment_amount)
                 if float(payment_amount) >su:
                     q={'user':user,'amount': pay_amount,'status':'paid','partial_status':False,'payment_type':'credit'}
                     serializer=transactionSerializer(data=q)
                     if serializer.is_valid():
                         serializer.save()
                         trans_logger.info(serializer.data)
                 l={key:payment_amount}
                 print("amount:",l,id)
                 j=[]
                 for pen,amount in l.items():
                     j.append(pen)
                     print("id,amount:",pen,amount)
                 value = (amount)
                 print("hot-value:",value)
                 print("id_list:",id)
                 sum1 = sum(id_amount[item] for item in id_amount)
                 print("sssss",sum1)
                 #payment_amount = serializer.data['payment_amount']
                 print("payment_amount:",payment_amount)
                 for key in id:
                    if key in id_amount:
                        del id_amount[key]
                 print('id_amount',id_amount)
                 partial_amount=abs(sum1-float(payment_amount))

                 pay_bill=transactions.objects.filter(id__in=id).update(status='paid',partial_status=False)
                 if len(s)>0:
                     d=y[-1:][0]
                     if d!=0:
                         x=[s[0]]
                         paybill=transactions.objects.filter(id__in=x).update(status='not_paid',partial_status=True)
                         id.extend(x)
                 #pay_bill.amount = abs(value)
                # pay_bill.save()
                 print("list:",id)
                 #queryset=[]
                 #for i in id:
                 payee=transactions.objects.filter(id__in=id).values()
                # sez=model_to_dict(payee)
                 print("payee:",payee)
                 queryset=[result for result in payee]
                 #print("queryset:",queryset)
                 logger.info(queryset)
                 for id in id:
                     pay = ({"payment_amount":payment_amount, "pay_via":pay_via, "partial_amount":partial_amount,"pay_status":pay_status,"user":user,'transaction':id})
                     serializer=paymentSerializer(data=pay)
                     if serializer.is_valid():
                         serializer.save()
                         pay_logger.info(serializer.data)
                         n=transactions.objects.all().last()
                         a=n.id
                         d=serializer.data['id']
                         print("pay_id:",serializer.data['id'])
                 if float(payment_amount)>sum1:
                     credit ={"user":user,"transaction":a,"payment":d,"extra_amount":partial_amount}
                     serializer=creditSerializer(data=credit)
                     if serializer.is_valid():
                         serializer.save()
                         credit_logger.info(serializer.data)
                 return JsonResponse({"success":True,"data":serializer.data})
                 pay_logger.error(serializer.errors)
                 return Response(serializer.errors)
         except Http404:
             return JsonResponse({"message":"data not added"})
