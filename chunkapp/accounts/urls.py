from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views


app_name = 'accounts'

urlpatterns = [
    
    path ('SignUp', views.SignUp, name='SignUp'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path ('logoutUser', views.logout_user, name='logout'),
]

