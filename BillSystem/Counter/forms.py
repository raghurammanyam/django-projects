from django import forms
from .models import Bill,Inventory

class Inventory_Form(forms.ModelForm):
    class Meta:
        model=Inventory
        fields = ('Rs2000','Rs500','Rs200','Rs100','Rs50','Rs10','Rs5','Rs2','Rs1')
class Bill_Form(forms.ModelForm):
    class Meta:
        model =Bill
        fields =('bill','amount')
