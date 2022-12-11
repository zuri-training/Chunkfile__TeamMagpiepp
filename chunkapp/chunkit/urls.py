from django.urls import path
from . import views

app_name = 'chunkit'

urlpatterns = [
    path('',views.landing, name='landing'),
    path('aboutUs/',views.aboutUs, name='aboutUs'),
    #path('PrivacyPolicy/', views.PrivacyPolicy, name='PrivacyPolicy'),
    #path('Faq/', views.Faq, name='Faq')
]