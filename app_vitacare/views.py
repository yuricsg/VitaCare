from django.shortcuts import render

def index(request):
    return render(request,'usuarios/index.html')

def login(request):
    return render(request, 'usuarios/login.html')

def register(request):
    return render(request, 'usuarios/register.html')