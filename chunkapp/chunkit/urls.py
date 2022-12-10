from django.urls import path

from . import views

urlpatterns = [
    path('',views.landing, name='landing'),
    #path('Aboutus/',views.Aboutus, name='Aboutus'),
    #path('PrivacyPolicy/', views.PrivacyPolicy, name='PrivacyPolicy'),
    #path('Faq/', views.Faq, name='Faq')
]