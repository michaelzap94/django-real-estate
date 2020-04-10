from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        messages.error(request, 'Test something')
        return render(request, 'register.html')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        messages.info(request, 'Test something')
        return render(request, 'login.html')
    else: 
        return render(request, 'login.html')

def logout(request):
    return redirect('index')

def dashboard(request):

    return render(request, 'dashboard.html', {})
