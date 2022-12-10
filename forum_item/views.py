from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from profile_page.models import Profile
from collection.models import Post
from forum_item.models import ForumComment
from forum_item.forms import ForumForm

# @login_required
def view_post(request, id):
    post = Post.objects.get(pk=id)
    user_loggedin = False
    if request.user.is_authenticated:
        user_loggedin = True

    if request.user.is_authenticated:
        user_loggedin = True

    context = { 
        'post': post,
        'user_loggedin': user_loggedin
    }

    return render(request, 'forum_item.html', context)

# @login_required()
@csrf_exempt
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        user_profile = Profile.objects.get(user=request.user)
        
        user_profile = Profile.objects.get(user=request.user)
        
        Post.objects.create(
            post_type='forum',
            author=user_profile,
            author_username=request.user.get_username(),
            title=title,
            content=content,
            upvotes=0,
            viewers=0,
            comments_count=0,
        )

        return HttpResponseRedirect(reverse('collection:forum'))

    return HttpResponseRedirect(reverse('landing_page:index'))
    # TODO uncomment
    # return HttpResponseRedirect(reverse('collection:forum'))

@login_required(login_url='/login/')
@csrf_exempt
def delete_post(request, id):
    user_profile = Profile.objects.get(user=request.user)
    post = Post.objects.get(id=id, author=user_profile)
    post.delete()

    return HttpResponseRedirect(reverse('collection:forum'))


