from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'accounts'

urlpatterns = [
    path ('SignUp', views.SignUp, name='SignUp'),
    path ('login', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    #path('successful/',views.successful, name='successful')
]