from django.shortcuts import render, redirect
from django.contrib.auth import  authenticate
from django.contrib.auth import login as auth_login

from django.contrib.auth.models import User
from django.contrib import messages



def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user)
        
            return redirect('chunkit:dashboard')

        else: 
            messages.info(request, ("There was an Error Logging In, Try Again.."))
            return redirect('login') 


    else:
        return render(request, 'login.html')


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