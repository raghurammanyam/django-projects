from rest_framework import serializers
from .models import Inventory,Bill
from collections import Counter
from django.forms.models import model_to_dict
import re

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'

class BillSerializer(serializers.ModelSerializer):
    class Meta():
        model = Bill
        fields = ('bill','amount','change','Rs2000','Rs500','Rs200','Rs100','Rs50','Rs10','Rs5','Rs2','Rs1')
        extra_kwargs = {'change':{'read_only':True,},'Rs2000':{'read_only':True,},'Rs500':{'read_only':True,},'Rs200':{'read_only':True,},'Rs100':{'read_only':True,},
                         'Rs50':{'read_only':True,},'Rs10':{'read_only':True,},'Rs5':{'read_only':True,},
                         'Rs2':{'read_only':True,},'Rs1':{'read_only':True,},}
    def create(self, validated_data):


         bill= validated_data['bill']
         amount = validated_data['amount']
         change = amount-bill
         get = change
         h=Inventory.objects.filter(id=2).first()
         g=model_to_dict(h)
         f={key:values for key,values in g.items() if key!='id' }
         print("delate:",f)
         inv=[re.findall(r'(\w+?)(\d+)', key)[0] for key,values in g.items() if key!='id']
         mon=[]
         z=f.values()
         print(z)
         for u,x in inv:
              mon.append(int(x))
         print("fuc:",(mon))
         dic=dict(zip(mon,z))
         print("zero:",dic)
         ram=Inventory.objects.filter(id=1).first()
         b=model_to_dict(ram)
         print("getting:",b)
         oat={key:values for key,values in b.items() if key!='id' }
         l=[]
         k=oat.keys()
         print(k)
         v=oat.values()
         print("values:",v)
         d=[re.findall(r'(\w+?)(\d+)', key)[0] for key,values in oat.items() if key!='id']
         print("fsfsbhdf:",d)
         for w,q in d:
             l.append(int(q))
         dip=l
         print("tictoe:",dip)
         denoms=sorted(l,reverse=True)
         cent=dict(zip(dip,v))
         print("combination:",cent)
         print("denoms:",denoms)
         """while (get > 0 and b['Rs2000']>0 and b['Rs500']>0 and b['Rs200']>0 and b['Rs100']>0 and b['Rs50']>0and b['Rs10']>0 and b['Rs5']>0 and b['Rs2']>0 and b['Rs1']>0):
             if (get >= denoms[0]):
                 num = get // denoms[0]
                 get -= denom[0]
                 dec={denoms[0]:num}
                 dic.update(dec)
                 print("bjbdfb:",dic)"""
             #denoms = denoms[1:]
         for i in denoms:
             if cent[i]>0:
                 while (get >= i and cent[i]>0):
                      num = get //i
                      get=get-i
                      dec={i:num}
                      dic.update(dec)
                      print("bjbdfb:",dic)
         lab={'Rs' + str(key):values for key,values in cent.items()}
         print("after loss:",lab)
         obj = Bill(bill=bill, amount=amount,change=change,Rs2000=dic[2000],Rs500=dic[500],Rs200=dic[200],Rs100=dic[100],Rs50=dic[50],Rs10=dic[10],Rs5=dic[5],Rs2=dic[2],Rs1=dic[1])
         obj.save()

         q=model_to_dict(obj)
         print("fgj:",q)
         v=dict(Counter(lab)-Counter(q))
         x =InventorySerializer(ram,data=v)
         if x.is_valid():
             x.save()
         return obj
