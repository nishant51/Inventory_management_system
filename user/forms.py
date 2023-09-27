from django.forms import fields
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import profile

class createuserform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class userupdateform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']

class profileupdateform(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['phone','address']
