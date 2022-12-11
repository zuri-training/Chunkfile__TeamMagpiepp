from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path ('SignUp/', views.SignUp, name='SignUp'),
    path ('login/', views.login, name='login'),
     path('successful/',views.successful, name='successful')
]