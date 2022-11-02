from django.shortcuts import render
from profile_page.models import Profile
from django.contrib.auth.models import User
from users.models import VerinvestUser
from django.contrib.auth.decorators import login_required

def show_profile(request):
    context = {
        'username' : request.user
    }

    return render(request, "profile.html", context)

def edit_profile(request):
    profile = VerinvestUser.objects.filter(username = "AnonymousUser").first()

    context = {
        'profile' : profile
    }
    return render(request, "modify.html", context)