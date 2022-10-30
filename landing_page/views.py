from operator import truediv
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.shortcuts import redirect


def index(request):
    user_loggedin = False
    if request.user.is_authenticated:
        user_loggedin = True
    
        context = {
            'user_loggedin': user_loggedin,
        }
        
        return render(request, 'index.html', context)
    else:
        return render(request,"landingpage.html")
    

def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('landing_page:login'))
    
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
            login(request,user)
            return redirect('landing_page:index')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

@login_required(login_url='login/')
def logout_user(request):
    logout(request)

    return HttpResponseRedirect(reverse('landing_page:login'))

