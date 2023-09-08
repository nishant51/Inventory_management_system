from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.contrib import messages
from django.contrib.auth import login as auth_login,logout,authenticate 
from django.contrib.auth.decorators import login_required
from .forms import createuserform,userupdateform,profileupdateform

# Create your views here.
def login(request):
     if request.method == 'POST':
         username =request.POST.get('username')
         password = request.POST.get('password')
         authenticated_user = authenticate(request,username = username, password = password)

         if  authenticated_user is not None:
             auth_login(request, authenticated_user)
             return redirect('dashboard-index')
         else:
             messages.info(request,'Provide information doesnot match our database')

     context ={}
     return render(request,'user/login.html',context)

def register(request):
   form = createuserform()
   if request.method == 'POST':
       form = createuserform(request.POST)
       if form.is_valid:
           form.save()
           user=form.cleaned_data.get('username')
           messages.success(request,'Account was created sucessfully ' + user +' continue to log in ')
           return redirect('user-login')
       else:     
           messages.success(request,'The User could not be created because the data didnot validate. ')
   else:
       form = createuserform()
       

   context = {
        'form':form
    }
   return render(request,'user/register.html',context)

def logoutpage(request):
    logout(request)
    return redirect('user-login')


def profile(request):
    return render(request,'user/profile.html')

def profile_update(request):
    if request.method == 'POST':
        u_form = userupdateform(request.POST,instance=request.user)
        p_form = profileupdateform(request.POST,request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('user-profile')
    else:
        u_form = userupdateform(instance=request.user)
        p_form = profileupdateform(instance=request.user.profile)
    context = {
        'u_form':u_form,
        'p_form':p_form,
        }
    return render(request,'user/profile_update.html',context)