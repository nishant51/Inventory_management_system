from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages

def index(request):
    return render(request,'dashboard/index.html')

def staff(request):
    return render(request,'dashboard/staff.html')

def product(request):
    return render(request,'dashboard/product.html')

def order(request):
    return render(request,'dashboard/order.html')

def login(request):
     return render(request,'user/login.html')

def register(request):
   form = createuserform()
   if request.method == 'POST':
       form = createuserform(request.POST)
       if form.is_valid:
           form.save()
           user=form.cleaned_data.get('username')
           messages.success(request,'Account was created sucessfully' + user)
           return redirect('user-login')
       else:
           form = createuserform()
   context = {
        'form':form
    }
   return render(request,'user/register.html',context)