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

def landing(request):
    return render(request, 'landing.html')


def login_user(request):
    if request.user.is_authenticated:
        return redirect('chunkit:landing')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)


            if user is not None:
                auth_login(request, user)
                return redirect('chunkit:dashboard')
            else:
                messages.info(request, "Password or email is incorrect")  

        return render(request, 'accounts/login.html')


def SignUp(request):
    
    if request.method == 'POST':
            fname = request.POST['fname']
            email = request.POST['email']
            username = request.POST['username']
            password = request.POST['password']

            user = User.objects.create_user(username=username, password=password, email=email)
            user.fname = fname
            user.save()
            return redirect('accounts:login')
    else:
            
            return render(request, 'SignUp.html') 
        



def logoutUser(request):
    auth_logout(request)
    return redirect('chunkit:landing')




def aboutUs(request):
    return render(request, 'aboutUs.html')

def contactUs(request):
    return render(request, 'contactUs.html')

def disclaimer(request):
    return render(request, 'disclaimer.html')

def setting(request):
    return render(request,'setting.html')

def termsOfUse(request):
    return render(request, 'termsOfUse.html')

def forgotpass(request):
    return render(request, 'forgotpass.html')


def password_reset_request(request):
    if request.method == 'POST':
        email = request.POST['email']
        user = User.objects.get(email=email)
        user.set_password(request.POST['password'])
        user.save()
        return redirect('accounts:login')
    else:
        return render(request, 'forgotpass.html')
    
