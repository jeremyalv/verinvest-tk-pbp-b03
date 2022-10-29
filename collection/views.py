from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers


from collection.models import Post

# @login_required
def show_collection(request):
    posts = Post.objects.all();
    context = {
        'posts': len(posts),
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

    context = {
        'forum_posts':forum_posts,
    }

    return render(request, 'forum.html', context)

# login required
def education_archive(request):
    education_posts = Post.objects.filter(post_type='education')

    context = {
        'education_posts':education_posts,
    }

    return render(request, 'education.html', context)

def get_json(request):
    posts = Post.objects.all()

    return HttpResponse(serializers.serialize("json", posts), content_type="application/json")

def get_forum_json(request):
    posts = Post.objects.filter(post_type='forum')

    return HttpResponse(serializers.serialize("json", posts), content_type="application/json")

def get_education_json(request):
    posts = Post.objects.filter(post_type='education')

    return HttpResponse(serializers.serialize("json", posts), content_type="application/json")
