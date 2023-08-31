from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='dashboard-index'),
    path ('staff',views.staff,name='dashboard-staff'),
    path('product',views.product,name='dashboard-product'),
    path('order/',views.order,name='dashboard-order'),
    path('login/',views.login,name='user-login'),
    path('register/',views.register,name='user-register'),
]