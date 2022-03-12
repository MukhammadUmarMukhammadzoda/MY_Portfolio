from http import client
from django.shortcuts import redirect, render
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
    services = Services.objects.all()

    return render(request, 'services.html', {'services': services} )

def resume(request):
    education = Education.objects.all()
    experience = Experiences.objects.all()
     
    data = {
        'education' : education,
        'experience' : experience
    }

    return render(request, 'resume.html', data )

def works(request):
    works = Projects.objects.all()

    return render(request, 'works.html', {"projects": works} )

def testimonials(request):
    clients = Clients.objects.all()


    return render(request, 'testimonials.html', {'clients': clients} )


def contact(request):
    if request.method == 'POST':
        contact = Contact()
        contact.name = request.POST.get('name')
        contact.email = request.POST.get('email')
        contact.title = request.POST.get('title')
        contact.message = request.POST.get('message')
        contact.save()
        return redirect('/')




    return render(request, 'contact.html' )
