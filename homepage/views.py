from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.utils import timezone

from .models import Project, Enquiry

def home(request):
    projects = Project.objects
    return render(request, 'homepage/home.html', {'projects': projects})

def add(request):
    projects = Project.objects
    if request.method == "POST":
        email = request.POST["email"]
        topic = request.POST["topic"]
        description = request.POST["description"]
        enquiry = Enquiry(enquiry_email = email, enquiry_topic = topic, enquiry_description = description, enquiry_date = timezone.now())
        enquiry.save()
    return render(request, 'homepage/home.html', {'projects': projects})
