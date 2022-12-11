from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def landing(request): #landing page
    return render(request, 'landing.html')

def aboutUs(request):
    return render(request, 'aboutUs.html')

def privacy(request):
    return render(request, 'privacy.html')

def contactUs(request):
    return render(request, 'contactUs.html')

def termsOfUse(request):
    return render(request, 'termsOfUse.html')       

def disclaimer(request):
    return render(request, 'disclaimer.html')     