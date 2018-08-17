from django import forms
from .models import Customers,categories,Items,Orders

class Customers_Form(forms.ModelForm):
    class Meta:
        model=Customers
        fields = ['name','Address','mobile_no']


class categories_Form(forms.ModelForm):
    class Meta:
        model=categories
        fields = ['name','status']

class Items_Form(forms.ModelForm):
    class Meta:
        model=Items
        fields = ['name','catogorie','price','Description','status']

class Orders_Form(forms.ModelForm):
    class Meta:
        model=Orders
        fields = ['Item','cust','catogorie','Total_price','Status']

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
