from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request,'dashboard/index.html')

def staff(request):
    return render(request,'dashboard/staff.html')

def product(request):
    return render(request,'dashboard/product.html')

def order(request):
    return render(request,'dashboard/order.html')