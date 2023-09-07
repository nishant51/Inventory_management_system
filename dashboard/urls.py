from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='dashboard-index'),
    path('costumer',views.costumer,name='dashboard-costumer'),
    path ('costumer/detail/<int:pk>',views.costumerdetail,name='dashboard-costumer-detail'),
    path('product',views.product,name='dashboard-product'),
    path('products/delete/<int:pk>/', views.product_delete,name='dashboard-products-delete'),
    path('products/update/<int:pk>/', views.product_edit,name='dashboard-products-update'),

    path('order/',views.order,name='dashboard-order'),
]