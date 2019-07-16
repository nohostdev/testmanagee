from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import Project

from django.shortcuts import render

def home(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, 'index.html', context)

def register(request):
    return render(request,'register.html')