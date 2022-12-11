from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def landing(request): #landing page
    return render(request, 'landing.html')

def aboutUs(request):
    return render(request, 'aboutUs.html')

#def PrivacyPolicy(request):
    return render(request, 'PrivacyPolicy.html')

#def Faq(request):
    return render(request, 'Faq.html')    