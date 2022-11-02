from django.shortcuts import render
from profile_page.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def show_profile(request):
    user_loggedin = False

    if request.user.is_authenticated:
        user_loggedin = True
    context = {
        'username' : request.user, 
        'user_loggedin': user_loggedin
    }

    return render(request, "profile.html", context)

def edit_profile(request):
    profile = Profile.objects.filter(user = request.user)
    user_loggedin = False

    if request.user.is_authenticated:
        user_loggedin = True

    context = {
        'profile' : profile,
        'user_loggedin' : user_loggedin
    }
    return render(request, "modify.html", context)