from django.shortcuts import render, redirect
from django.contrib.auth import  authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.views import LoginView




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
            return redirect('accounts:login_user')
    else:
            
            return render(request, 'SignUp.html') 
        
           


def logoutUser(request):
    auth_logout(request)
    return redirect('chunkit:landing')