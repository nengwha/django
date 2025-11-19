from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse


from django.http import HttpResponse
from django.shortcuts import redirect


HARDCODED_USER = 'user'
HARDCODED_PASS = 'password123'

def index(request):
    message = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == HARDCODED_USER and password == HARDCODED_PASS:
            return redirect('login:success')
        else:
            message = 'Invalid username or password.'
    return render(request, 'login/index.html', {'message': message})

def success(request):
    return render(request, 'login/success.html')