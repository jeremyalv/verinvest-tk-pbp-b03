from django.shortcuts import render, redirect
from profile_page.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import ast
import datetime

@login_required(login_url="{% url 'landing_page:login' %}")
def show_profile(request):
    user_loggedin = False

    if request.user.is_authenticated:
        user_loggedin = True
    context = {
        'username' : request.user.username, 
        'user_loggedin': user_loggedin
    }

    return render(request, "profile.html", context)

@login_required(login_url="{% url 'landing_page:login' %}")
def edit_profile(request):
    user_profile = Profile.objects.get(user = request.user)
    user_loggedin = False

    if request.user.is_authenticated:
        user_loggedin = True

    context = {
        'profile' : user_profile,
        'user_loggedin' : user_loggedin
    }
    return render(request, "modify.html", context)

def get_profile_json(request):
    user = User.objects.get(username = "dummy")
    profile = Profile.objects.get(user = user)

    return HttpResponse(serializers.serialize("json", [profile]), content_type="application/json")

@csrf_exempt
def edit_firstname(request):
    user = User.objects.get(username = "dummy")
    profile = Profile.objects.get(user = user)

    profile.first_name = ast.literal_eval(request.body.decode('utf-8'))["name"]
    profile.save()

    return redirect('profile_page:get_profile_json')

@csrf_exempt
def edit_lastname(request):
    user = User.objects.get(username = "dummy")
    profile = Profile.objects.get(user = user)

    profile.last_name = ast.literal_eval(request.body.decode('utf-8'))["name"]
    profile.save()

    return redirect('profile_page:get_profile_json')

@csrf_exempt
def edit_email(request):
    user = User.objects.get(username = "dummy")
    profile = Profile.objects.get(user = user)

    profile.email = ast.literal_eval(request.body.decode('utf-8'))["name"]
    profile.save()

    return redirect('profile_page:get_profile_json')

@csrf_exempt
def edit_birthdate(request):
    user = User.objects.get(username = "dummy")
    profile = Profile.objects.get(user = user)

    date = ast.literal_eval(request.body.decode('utf-8'))["name"]
    profile.birth_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
    profile.save()

    return redirect('profile_page:get_profile_json')

@csrf_exempt
def edit_occupation(request):
    user = User.objects.get(username = "dummy")
    profile = Profile.objects.get(user = user)

    profile.occupation = ast.literal_eval(request.body.decode('utf-8'))["name"]
    profile.save()

    return redirect('profile_page:get_profile_json')