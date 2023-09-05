from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
 path('login/',views.login,name='user-login'),
 path('register/',views.register,name='user-register'),
 path('logout/', views.logoutpage, name='logout'),
 path('profile/',views.profile,name='user-profile'),
 path('profile_update/',views.profile_update,name='user-profile-update'),

]