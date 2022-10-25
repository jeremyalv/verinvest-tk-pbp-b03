from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from collection.models import Post, Comment

# @login_required
def show_collection(request):
    context = {}
    
    return render(request, 'collection.html', context)

# login required
def forum_archive(request):

    return render(request, 'forum.html')

# login required
def education_archive(request):

    return render(request, 'education.html')

""" fixed ver
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
"""

