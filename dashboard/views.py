from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product,Order
from .form import *
from django.contrib.auth.models import User
from django.contrib import messages
from .decorators import auth_users, allowed_users


@login_required(login_url='user-login')
def index(request):
    orders = Order.objects.all()
    products = Product.objects.all()
    costumers = User.objects.all()
    costumer_count = costumers.count()
    product_count = products.count()
    order_count = orders.count()
    if request.method =='POST':
            form =orderform(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.costumer = request.user
                instance.save()
                return redirect('dashboard-index')
    else:
        form = orderform()
    context = {
        'orders' :orders,
        'form':form,
        'product':products,
        'costumer_count':costumer_count,
        'product_count':product_count,
        'order_count':order_count,
        }
    return render(request,'dashboard/index.html',context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def costumer(request):
    costumers = User.objects.all()
    orders = Order.objects.all()
    products = Product.objects.all()
    costumer_count = costumers.count()
    product_count = products.count()
    order_count = orders.count()
    context = {
        'costumers':costumers,
        'costumer_count':costumer_count,
        'product_count':product_count,
        'order_count':order_count,
    }
    return render(request,'dashboard/costumer.html',context)

@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def costumerdetail(request,pk):
    costumers = User.objects.get(id=pk)
    context = {
        'costumers':costumers,
    }
    return render(request,'dashboard/costumerdetail.html',context)

@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def product(request):
    costumers = User.objects.all()
    orders = Order.objects.all()
    products = Product.objects.all()
    costumer_count = costumers.count()
    product_count = products.count()
    order_count = orders.count()
    if request.method == 'POST':
        form = productform(request.POST)
        if form.is_valid:
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            return redirect('dashboard-product')
    else:
        form =productform()
    items = Product.objects.all()
    context = {
        'items': items,
        'form':form,
        'costumer_count':costumer_count,
        'product_count':product_count,
        'order_count':order_count,
    }
    return render(request,'dashboard/product.html',context)

@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def product_edit(request, pk):
    item =Product.objects.get(id=pk)
    if request.method =='POST':
        form = productform(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = productform(instance=item)
    context = {
        'form':form,
        'pk':pk
    }
    return render(request, 'dashboard/productedit.html', context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')
    context = {
        'item': item
    }
    return render(request, 'dashboard/deleteproduct.html', context)
        
@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def order(request):
    orders= Order.objects.all()
    costumers = User.objects.all()
    products = Product.objects.all()
    costumer_count = costumers.count()
    product_count = products.count()
    order_count = orders.count()
    context = {
        'orders':orders,
        'costumer_count':costumer_count,
        'product_count':product_count,
        'order_count':order_count,
    }
    return render(request,'dashboard/order.html',context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def alltables(request):
    items = Product.objects.all()
    orders= Order.objects.all()
    costumers = User.objects.all()
    products = Product.objects.all()
    context = {
     'orders':orders,
     'items': items,
     'costumers':costumers,
     'orders' :orders,
     'product':products,
    }
    return render(request,'tables.html',context)

def aboutus(request):
    return render(request,'aboutus.html')