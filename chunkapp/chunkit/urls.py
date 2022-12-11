from django.urls import path
from . import views

app_name = 'chunkit'

urlpatterns = [
    path('',views.landing, name='landing'),
    path('aboutUs/',views.aboutUs, name='aboutUs'),
    path('privacy/',views.privacy, name='privacy'),
    path('contactUs/',views.contactUs, name='contactUs'),
    path('termsOfUse/',views.termsOfUse, name='termsOfUse'),
    path('disclaimer/',views.disclaimer, name='disclaimer')
    
]