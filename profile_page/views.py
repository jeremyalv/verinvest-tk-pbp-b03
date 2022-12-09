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
    user = User.objects.get(username = "dummy")
    # user = User.objects.create(
    #     username = "dummy",
    #     first_name = "John",
    #     last_name = "Doe",
    #     email = "dummy@gmail.com",
    # )

    profile = Profile.objects.create(
                user = user,
                first_name = user.first_name,
                last_name = user.last_name,
                email = user.email,
                is_expert = user.is_staff,
                birth_date = None,
                occupation = None,
            )

    return HttpResponse(serializers.serialize("json", profile), content_type="application/json")