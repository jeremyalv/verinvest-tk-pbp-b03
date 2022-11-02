from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.decorators import login_required

from collection.models import Post

def show_collection(request):
    posts = Post.objects.all()
    user_loggedin = False
    if request.user.is_authenticated:
        user_loggedin = True

    context = {
        'posts': posts,
        'count': posts.count(),
        'user_loggedin': user_loggedin,
    }
    
    return render(request, 'collection.html', context)

def search_collection(request, search_key):
    filtered_posts = Post.objects.filter(title_icontains=search_key)
    template = ''

    if ("forum" in request.path):
        template = 'forum.html'    
    elif ("education" in request.path):
        template = 'education.html'
    else:
        template = 'collection.html'

    context = {
        'filtered_posts': filtered_posts,
    }

    return render(request, template, context)

# login required
def forum_archive(request):
    forum_posts = Post.objects.filter(post_type='forum')
    user_loggedin = False
    if request.user.is_authenticated:
        user_loggedin = True

    context = {
        'forum_posts': forum_posts,
        'count': forum_posts.count(),
         'user_loggedin': user_loggedin,
    }

    return render(request, 'forum.html', context)

# login required
def education_archive(request):
    education_posts = Post.objects.filter(post_type='education')
    user_loggedin = False
    if request.user.is_authenticated:
        user_loggedin = True

    context = {
        'forum_posts': education_posts,
        'count': education_posts.count(),
         'user_loggedin': user_loggedin,
    }

    return render(request, 'education.html', context)

def get_json(request):
    posts = Post.objects.all()

    return HttpResponse(serializers.serialize("json", posts, 
                        use_natural_foreign_keys=True,
                        use_natural_primary_keys=True), 
                        content_type="application/json")

def get_forum_json(request):
    posts = Post.objects.filter(post_type='forum')

    return HttpResponse(serializers.serialize("json", posts,
                        use_natural_foreign_keys=True,
                        use_natural_primary_keys=True), 
                        content_type="application/json")

def get_education_json(request):
    posts = Post.objects.filter(post_type='education')

    return HttpResponse(serializers.serialize("json", posts,
                        use_natural_foreign_keys=True,
                        use_natural_primary_keys=True),
                        content_type="application/json")
