import email
from django.shortcuts import render, redirect
from django.contrib.auth import  authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.decorators import login_required



def SignUp(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        username = request.POST['username']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('chunkit:dashboard')
            else:
                messages.error(request, 'Username or password is incorrect')
                return redirect('chunkit:landing')
            
        else:
            messages.error(request, 'Username or password is incorrect')
            return redirect('chunkit:landing')
        
    else:
        return render(request,'SignUp.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect('chunkit:dashboard')
            else:
                messages.error(request, 'Username or password is incorrect')
                return redirect('chunkit:landing')
           
        else:
            messages.error(request, 'Username or password is incorrect')
            return redirect('chunkit:landing')
        
    else:
        return render(request,'login.html')
    


def logout_user(request):
    auth_logout(request)
    return redirect('chunkit:landing')




