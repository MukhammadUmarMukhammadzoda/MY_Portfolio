from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):

    return render(request, 'index.html')



def welcome(request):

    return render(request, 'welcome.html' )



def about(request):
    skills = Skills.objects.all()

    return render(request, 'about.html', {"skills": skills} )


def services(request):

    return render(request, 'services.html' )

def resume(request):

    return render(request, 'resume.html' )

def works(request):

    return render(request, 'works.html' )

def testimonials(request):

    return render(request, 'testimonials.html' )


def contact(request):

    return render(request, 'contact.html' )
