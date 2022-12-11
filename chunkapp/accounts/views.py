from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
 

def SignUp(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        email = request.POST.get('email')
        username = request.POST.get('uname')
        password = request.POST.get('pass')

        NewUser = User.objects.create_user(username= username, email=email, password=password)
        NewUser.full_name = fname

        NewUser.save()
        return redirect('login')
    else:
        return render (request, 'SignUp.html' )

    
    


def login(request):
    return render (request, 'login.html' )    
