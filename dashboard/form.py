from django import forms
from django.forms import fields
from django.forms import ModelForm
from .models import Product,Order

class productform(forms.ModelForm):
    class Meta:
        model =Product
        fields = ['name','category','quanitiy']


class orderform(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name','orderquantity']