from django.shortcuts import render
from django.contrib.auth import authenticate, login

from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def register(request):
    return render(request,'register.html')