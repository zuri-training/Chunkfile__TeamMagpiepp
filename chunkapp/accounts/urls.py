from django.urls import path
from unicodedata import name
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView

app_name = 'accounts'

urlpatterns = [
    
    path ('SignUp', views.SignUp, name='SignUp'),
    path ('login_user/', LoginView.as_view(template_name='login.html'), name='login_user'),
    path ('logoutUser', views.logoutUser, name='logout'),
    path ('aboutUs/', views.aboutUs, name='aboutUs'),
    path ('forgotpass/', views.forgotpass, name='forgotpass'),
    
]

