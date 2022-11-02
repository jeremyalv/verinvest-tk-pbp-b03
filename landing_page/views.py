from pickle import NONE
from types import NoneType
from django.forms import NullBooleanField
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
# from .models import CustomUser
from .forms import RegisterForm
from profile_page.models import Profile
from django.contrib.auth.decorators import login_required, permission_required


def navigation(request):
    user_loggedin = False

    if request.user.is_authenticated:
        username = request.user
        # user = CustomUser.objects.filter(username = user.username)
        user = Profile.objects.get(user = request.user)
        user_loggedin = True

        context = {
            'user_loggedin': user_loggedin,
            'username': request.user,
            'user': user,
        }

        return render(request, 'header.html', context)
    
    context = {
        'user_loggedin': user_loggedin,
    }

    render(request, 'header.html', context)

def index(request):
    # users = CustomUser.objects.all()
    users = Profile.objects.all()
    user_loggedin = False

    if request.user.is_authenticated:
        user_loggedin = True

        context = {
            'user_loggedin': user_loggedin,
            'username': request.user.get_username(),
            'users': users,
            'user_count': len(users),
        }
            
        return render(request, 'index.html', context)
    
    context = { 
        'user_loggedin': user_loggedin ,
        'users': users,
        'user_count': len(users),
        }
    return render(request, 'index.html', context)  

def register(request):
    form = RegisterForm()
    user_loggedin = False

    if request.user.is_authenticated:
        user_loggedin = True

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            # custom_user = CustomUser.objects.create(
            #     user=user,
            #     first_name=user.first_name,
            #     last_name=user.last_name,
            #     email=user.email,
            #     is_expert=user.is_expert,
            # )

            Profile.objects.create(
                user = user,
                first_name = user.first_name,
                last_name = user.last_name,
                email = user.email,
                is_expert = user.is_expert,
                birth_date = None,
                occupation = None,
            )

            return HttpResponseRedirect(reverse('landing_page:login'))
    user_loggedin = False

    if request.user.is_authenticated:
        user_loggedin = True

    context = {
        'form': form,
        'user_loggedin': user_loggedin
    }

    return render(request, 'register.html', context)

def login_user(request):
    user_loggedin = False

    if request.user.is_authenticated:
        user_loggedin = True
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('landing_page:index'))

    context = {
        'user_loggedin': user_loggedin
    }

    return render(request, 'login.html', context)

@login_required(login_url="{% url 'landing_page:login' %}")
def logout_user(request):
    logout(request)

    return HttpResponseRedirect(reverse('landing_page:index'))

