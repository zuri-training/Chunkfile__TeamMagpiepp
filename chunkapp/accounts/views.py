from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
 

def SignUp(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        email = request.POST['email']
        username = request.POST['uname']
        password = request.POST['pass']

        NewUser = User.objects.create_user(username= username, email=email, password=password)
        NewUser.full_name = fname

        NewUser.save()
        return redirect('login')
    else:
        return render (request, 'SignUp.html' )

    
    


def login(request):
    return render (request, 'login.html' )    


def successful(request):
    return render (request, 'successful.html')    
