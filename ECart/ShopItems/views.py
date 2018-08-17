from django.shortcuts import render,render_to_response,redirect
from django.http import JsonResponse,HttpResponse,HttpResponseNotFound
from  django.db.models import Q,Count, Avg ,Max,Sum, Count
from .models import Customers,categories,Items,Orders
from django.core import serializers
from .forms import Customers_Form,categories_Form,Items_Form,Orders_Form
from django.template import Context,loader,RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from .forms import SignupForm
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.core.mail import send_mail
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
def asn(request):
    act = Customers.objects.all()
    print (act)
    if act:
        context = {
            'act': act
        }
        return render(request, 'ECart.html', context)
    else:
        return HttpResponseNotFound("not found")



def fun(request):
    fun = categories.objects.all()
    print (fun)
    if fun:
        context = {
            'fun': fun
        }
        return render(request, 'ECart.html', context)
    else:
        return HttpResponseNotFound("not found")



def ram(request):
    cat = Items.objects.all()
    print (cat)
    if cat:
        context = {
            'cat': cat
        }
        return render(request, 'ECart.html', context)
    else:
        return HttpResponseNotFound("not found")




def price(request):
    ord = Orders.objects.all()
    print (ord)
    if ord:
        context = {
            'ord': ord
        }
        return render(request, 'ECart.html', context)
    else:
        return HttpResponseNotFound("not found")


def hat(request,_name):
     fun = categories.objects.filter(name=_name)
     print (fun)
     if fun:
        context = {
            'fun': fun
        }
        return render(request, 'ECart.html', context)
     else:
         return HttpResponseNotFound("not found")

def bot(request,_range):
     start,end = [int(x) for x in _range.split('-')]
     ord = Orders.objects.filter(Q(Total_price__gte=start)&Q(Total_price__lte=end))
     print (ord)
     if ord:
        context = {
            'ord': ord
        }
        return render(request, 'Ecart.html', context)
     else:
         return HttpResponseNotFound("not found")



def lab(request,_range):
     start,end = [int(x) for x in _range.split('-')]
     cat = Items.objects.filter(Q(price__gte=start)&Q(price__lte=end))
     print (cat)
     if cat:
        context = {
            'cat': cat
        }
        return render(request, 'ECart.html', context)
     else:
         return HttpResponseNotFound("not found")
def can(request,_name):
     cat = Items.objects.filter(name=_name)
     print (cat)
     if cat:
        context = {
            'cat': cat
        }
        return render(request, 'ECart.html', context)
     else:
         return HttpResponseNotFound("not found")

def rank(request):
     ord = Orders.objects.all().values('cust').annotate(total_price=Sum('Total_price')).order_by('total_price')

     print (ord)
     if ord:
        context = {
            'ord': list(ord)
        }
        return JsonResponse(context)

def tac(request,_price):
    cat = Items.objects.all().filter(Q(price__gte=_price))
    print (cat)
    if cat:
       context = {
           'cat': cat
       }
       return render(request, 'ECart.html', context)
    else:
        return HttpResponseNotFound("not found")




def part(request,_name):
    act = Customers.objects.all().filter(name=_name)
    print (act)
    if act:
       context = {
           'act': act
       }
       return render(request, 'shop.html', context)
    else:
        return HttpResponseNotFound("not found")



def nat(request,_id):
     ord = Orders.objects.filter(id=_id)
     print (ord)
     if ord:
        context = {
            'ord': ord
        }
        return render(request, 'shop.html', context)
     else:
         return HttpResponseNotFound("not found")


def wir(request,_status):
     cat = Items.objects.filter(status=_status)
     print (cat)
     if cat:
        context = {
            'cat': cat
        }
        return render(request, 'shop.html', context)
     else:
         return HttpResponseNotFound("not found")

def mar(request):
     hat = Orders.objects.all().values('cust').annotate(total_price=Sum('Total_price')).order_by('total_price')

     print (hat)
     if hat:
        context = {
            'hat': hat
        }
        return render(request, 'ECart.html', context)
     else:
        return HttpResponseNotFound("not found")


def cost(request):

    act = Customers_Form(request.POST or None, request.FILES or None)
    if act.is_valid():
        instance = act.save(commit=False)
        instance.save()
        return HttpResponse('form submited')
    return render(request, 'ECart.html', {'act': act})


def app(request):

    fun = categories_Form(request.POST or None, request.FILES or None)
    if fun.is_valid():
        instance = fun.save(commit=False)
        instance.save()
        return HttpResponse('form submited')
    return render(request, 'ECart.html', {'fun': fun})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
            'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'basic.html', {'form': form})
def activate(request, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
# Create your views here.
