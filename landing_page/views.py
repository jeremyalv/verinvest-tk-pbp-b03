from operator import truediv
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required, permission_required


def index(request):
    user_loggedin = False
    if request.user.is_authenticated:
        user_loggedin = True
    
    context = {
        'user_loggedin': user_loggedin,
    }
        
    return render(request, 'index.html', context)
    

def register(request):
    if request.method == 'POST':
        form = RegisterForm()

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('landing_page:login'))
    else:
        form = RegisterForm()
    context = {
        'form' : form,
    }

    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return HttpResponseRedirect(reverse('landing_page:index'))
    
    return render(request, 'login.html')

@login_required(login_url='login/')
def logout_user(request):
    logout(request)

    return HttpResponseRedirect(reverse('landing_page:login'))

