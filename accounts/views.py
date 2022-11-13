from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.db import IntegrityError

def signupaccount(request):
    return render(request, 'signup_account.html', {'form':UserCreationForm})

def logoutaccount(request):        
    logout(request)
    return redirect('home')

def loginaccount(request):
    return render(request, 'login_account.html')
