from django.shortcuts import render
from profile_page.models import Profile
from django.contrib.auth.decorators import login_required

def show_profile(request):
    context = {
        'username' : request.user
    }

    return render(request, "profile.html", context)

@login_required(login_url='landing_page:login')
def edit_profile(request):
    profile = Profile.objects.filter(user = request.user)

    context = {
        'profile' : profile
    }
    return render(request, "modify.html", context)