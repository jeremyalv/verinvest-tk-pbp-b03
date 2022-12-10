import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, JsonResponse
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

from collection.models import Post
from profile_page.models import Profile
from profile_page.models import Profile

def show_collection(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        search_key = request.GET.get('search_key')

        user_loggedin = False

        if request.user.is_authenticated:
            user_loggedin = True

        context = {
            'user_loggedin': user_loggedin,
            'search_key': search_key,
            'count': len(posts),
        }
        
        return render(request, 'collection.html', context)
    return HttpResponseBadRequest("Bad request")

@csrf_exempt
def get_collections_mobile(request):
    if request.method == 'GET':
        posts = Post.objects.all()

        return JsonResponse({
            'posts': posts,
        })
    else:
        return HttpResponseBadRequest("Bad request")


@csrf_exempt
def search_collection(request):
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
        
@csrf_exempt
def search_collection_mobile(request):
    if request.method == 'GET':
        search_key = request.GET.get('search_key')
        if search_key is None:
            data = json.loads(request.body)
            search_key = data['search_key']
        
        if search_key is not None:
            posts = Post.objects.filter(title__icontains=search_key)
    else:
        return HttpResponseBadRequest("Bad request")



# login required
def forum_archive(request):
    if request.method == 'GET':
        forum_posts = Post.objects.filter(post_type='forum')
        search_key = request.GET.get('search_key')

        user_loggedin = False
        
        if request.user.is_authenticated:
            user_loggedin = True

        context = {
            'user_loggedin': user_loggedin,
            'search_key': search_key,
            'count': forum_posts.count(),
        }
        
        return render(request, 'forum.html', context)
    return HttpResponseBadRequest("Bad request")

# login required
def education_archive(request):
    if request.method == 'GET':
        edu_posts = Post.objects.filter(post_type='education')
        search_key = request.GET.get('search_key')

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
