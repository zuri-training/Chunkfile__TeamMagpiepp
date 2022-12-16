import email
from django.shortcuts import render, redirect
from django.contrib.auth import  authenticate, login, logout
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.decorators import login_required

def landing(request):
    return render(request, 'landing.html')

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
            return redirect('chunkit:dashboard')
        else:
            messages.error(request, 'Username or password is incorrect')
            return redirect('chunkit:landing')
        return render(request,'SignUp.html')
    else:
        return render(request,'SignUp.html')
    
def login_user(request):
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
            return redirect('chunkit:dashboard')
        else:
            messages.error(request, 'Username or password is incorrect')
            return redirect('chunkit:landing')
        return render(request,'login.html') 
    else:
        return render(request,'login.html')
    


def logout_user(request):
    auth_logout(request)
    return redirect('chunkit:landing')



def password_reset_request(request):
    if request.method == 'POST':
        email = request.POST['email']
        user = User.objects.get(email=email)
        user.set_password(request.POST['password'])
        user.save()
        return redirect('accounts:login')
    else:
        return render(request, 'forgotpass.html')
    
