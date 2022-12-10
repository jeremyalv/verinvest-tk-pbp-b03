from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

from collection.models import Post
from profile_page.models import Profile

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
    if request.method == 'GET':
        search_key = request.GET.get('search_key')
        posts = Post.objects.filter(title__icontains=search_key)
        template = ''

        if ("forum" in request.path):
            template = 'forum.html'    
        elif ("education" in request.path):
            template = 'education.html'
        else:
            template = 'collection.html'

        context = {
            'posts': posts,
        }

        return render(request, template, context)

# login required
def forum_archive(request):
    forum_posts = Post.objects.filter(post_type='forum')
    user_loggedin = False
    if request.user.is_authenticated:
        user_loggedin = True

    context = {
        'education_posts': forum_posts,
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

def viewuser(request):
    post = Post.objects.get(pk=1)
    user = Profile.objects.get(user=request.user)
    
    postjson = model_to_dict(post)
    userjson = model_to_dict(user)

    postjson["author"] = userjson

    # Post JSON now has author with value json
    return JsonResponse({'post': postjson})

    # return HttpResponse(serializers.serialize("json", user), content_type="application/json") 

def get_json(request):
    if request.method == 'GET':
        post_list = []
        search_key = request.GET.get('search_key')

        if search_key is None:
            posts = Post.objects.all()
        else:
            posts = Post.objects.filter(title__icontains=search_key)

        return HttpResponse(serializers.serialize("json", posts, 
                                use_natural_foreign_keys=True,
                                use_natural_primary_keys=True), 
                                content_type="application/json")            

    else:
        return HttpResponseBadRequest("Bad request")

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
