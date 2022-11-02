from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.shortcuts import redirect
from django.core import serializers
from .models import Fortofolio
import datetime


def index(request):
    user_loggedin = False

    if request.user.is_authenticated:
        user_loggedin = True
        
        user = User.objects.get(username=request.user.username)
        context = {
            'user_loggedin': user_loggedin,
            'first_name' : request.user.first_name,
            'last_name' : request.user.last_name,
            'username' : request.user.username,
            'last_login': request.COOKIES['last_login'],
            
        }
            
        return render(request, 'index.html', context)
    
    context = { 'user_loggedin': user_loggedin }
    return render(request, 'index.html', context)  

def register(request):
    form = UserCreationForm()
    user_loggedin = False
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print(request.POST)
            form.save()
            user = User.objects.get(username=request.POST['username'])
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.user_type = request.POST['user_type']
            user.save()
            return HttpResponseRedirect(reverse('landing_page:login'))
        
    context = {
        'form': form,
        'users': User.objects.all(),
        'user_loggedin': user_loggedin
    }
    return render(request, 'register.html', context)
            

# def register(request):
#     if request.method == 'POST':
#         form = RegisterForm()

#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('landing_page:login'))
#     else:
#         form = RegisterForm()
#     context = {
#         'form' : form,
#     }

#     return render(request, 'register.html', context)

def login_user(request):
    user_loggedin = False
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse('landing_page:index'))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    context = { 'user_loggedin': user_loggedin }
    return render(request, 'login.html',context)

@login_required(login_url='login/')
def logout_user(request):
    logout(request)

    return HttpResponseRedirect(reverse('landing_page:index'))

@login_required(login_url='landing_page:login')
def forto(request):
    user_loggedin = False

    if request.user.is_authenticated:
        user_loggedin = True
        
        user = User.objects.get(username=request.user.username)
        context = {
            'user_loggedin': user_loggedin,
            'first_name' : request.user.first_name,
            'last_name' : request.user.last_name,
            'username' : request.user.username,
            
        }
            
        return render(request, 'forto.html', context)
    
    context = { 'user_loggedin': user_loggedin }
    return render(request, 'index.html', context) 

def show_forto_json(request):
    # mengembalikan semua data task dalam bentuk json (Task 6)
    data = Fortofolio.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json") 

@login_required(login_url='landing_page:login')
def create_forto_modal(request):
    if request.method == "POST":
        print("ini")
        user = User.objects.filter(username=request.user.username)
        nama = request.POST.get('nama')
        jumlah = request.POST.get('jumlah')
        forto = Fortofolio(user=user, nama= nama, jumlah=jumlah)
        forto.save()
        return redirect('landing_page:forto')
    return HttpResponse("")

def delete_forto_ajax(request, id):
    forto = Fortofolio.objects.get(id=id)
    forto.delete()
    return redirect('landing_page:forto')

