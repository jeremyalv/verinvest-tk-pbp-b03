from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from profile_page.models import Profile
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from collection.models import Post

@login_required(login_url="{% url 'landing_page:login' %}")
def show_profile(request):
    user = Profile.objects.get(user = request.user)
    posts = Post.objects.filter(author = user)

    user_loggedin = False

    if request.user.is_authenticated:
        user_loggedin = True
    context = {
        'username' : request.user.username, 
        'user_loggedin': user_loggedin,
        'posts': posts
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

@login_required(login_url="{% url 'landing_page:login' %}")
def edit_name(request):
    user_profile = Profile.objects.get(user = request.user)
    user_profile.first_name = request.POST.get('first_name')
    user_profile.last_name = request.POST.get('last_name')
    user_profile.save()

    return HttpResponseRedirect(reverse('show_profile'))