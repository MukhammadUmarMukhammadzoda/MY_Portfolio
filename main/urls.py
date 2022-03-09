from unicodedata import name
from django import views
from django.urls import path
from . import views


urlpatterns = [
    
    path('',views.index, name='index'),
    path('welcome', views.welcome, name='welcome'),
    path('about',views.about, name='about'),
    path('services',views.services, name='services'),
    path('resume',views.resume, name='resume'),
    path('works',views.works,name='works'),
    path('testimonials',views.testimonials, name='testimonials'),
    path('contact',views.contact, name='contact')
    
    ]