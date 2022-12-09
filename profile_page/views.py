from django.shortcuts import render
from profile_page.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core import serializers

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
    profile = Profile.objects.filter(pk=1)
    
    return HttpResponse(serializers.serialize("xml", profile), content_type="application/xml")