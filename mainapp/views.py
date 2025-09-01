from django.shortcuts import render
from .models import BaseDetail, Homepage, Team, AboutUs, Project, JobOpening, ContactUs

base_detail = BaseDetail.objects.first()
context = {'base_detail': base_detail}

def home(request):
    homepage = Homepage.objects.first()
    context['homepage'] = homepage
    return render(request, 'mainapp/home.html', context)

def about(request):
    about_us = AboutUs.objects.first()
    teams = Team.objects.all()
    context['about_us'] = about_us
    context['teams'] = teams
    return render(request, 'mainapp/about.html', context)

def projects(request):
    projects = Project.objects.all()
    context['projects'] = projects
    return render(request, 'mainapp/projects.html', context)

def careers(request):
    job_openings = JobOpening.objects.filter(status=True)
    context['job_openings'] = job_openings
    return render(request, 'mainapp/career.html', context)

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact_entry = ContactUs(name=name, email=email, phone=phone, subject=subject, message=message)
        if contact_entry:
            contact_entry.save()
            return render(request, 'mainapp/contact.html', {'success': True, 'base_detail': base_detail})
    return render(request, 'mainapp/contact.html', context)
