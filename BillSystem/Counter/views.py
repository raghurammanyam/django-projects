from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseNotFound
from .models import Bill,Inventory
from .forms import Inventory_Form,Bill_Form
from django.forms.models import model_to_dict
from collections import Counter
from django.views.decorators.csrf import csrf_exempt

def Inven(request):
    act = Inventory.objects.all()
    print (act)
    if act:
        context = {
            'act': act
        }
        return render(request,'bill.html',context)
    else:
        return HttpResponseNotFound("not found")

@csrf_exempt
def cost(request):
    act= Inventory_Form(request.POST)
    posting=request.POST
    #print(posting)
    post={}
    a=Inventory.objects.filter(id=1).first()
    b=model_to_dict(a)
    print("getting:",b)
    print("---------------------------------------------------------------")
    for key,values in posting.items():
       val=values
       for x in val:
           if key!='csrfmiddlewaretoken':
               y=int(x)
               d={key:y}
               post.update(d)
       print("post data:",post)
       print("---------------------------------------------------------------")
    z=dict(Counter(b)+Counter(post))
    print("combined value:",z)
    if act.is_valid():
        act= Inventory_Form(z,instance=a)
        act.save()
        return HttpResponse('form submited')
    return render(request, 'bill.html', {'act': act})

def app(request):
    act = Inventory_Form(request.POST or None, request.FILES or None)
    print(act)
    if act.is_valid():
        instance = act.save()
        instance.save()
        return HttpResponse('form submited')
    return render(request, 'bill.html', {'act': act})

def pay(request):
    pay = Bill.objects.all()
    print (pay)
    if pay:
        context = {
            'pay': pay
        }
        return render(request,'bill.html',context)
    else:
        return HttpResponseNotFound("not found")

def test(request):
    instance=Inventory.objects.filter(id=1).first()
    print("this instance data  :",instance)
    pay= Bill_Form(request.POST)
    posting=request.POST
    post={}
    for key,values in posting.items():
       val=values
       for x in val:
           if key!='csrfmiddlewaretoken':
               y=int(x)
               d={key:y}
               post.update(d)
    print("posted data:",post)               

    b=model_to_dict(instance)
    print(b)
    if pay.is_valid():
        pay= Inventory_Form(pay)
        pay.save()
        print(z)
        return HttpResponse('form submited')
    return render(request, 'bill.html', {'pay': pay})
