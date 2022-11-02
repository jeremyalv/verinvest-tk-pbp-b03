from datetime import datetime
from xml.etree.ElementTree import Comment
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from collection.models import Post
from forum_item.models import ForumComment, Reply

# @login_required
def view_post(request, id):
    post = Post.objects.get(pk=id)

    context = { 'post': post }

    return render(request, 'forum_item.html', context)

@login_required()
@csrf_exempt
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        date = datetime.now()


        Post.objects.create(
            post_type='forum',
            author=request.user,
            title=title,
            content=content,
            upvotes=0,
            viewers=0,
            comments_count=0,
            date=date,
        )

        return HttpResponseRedirect(reverse('collection:forum'))

    return HttpResponseRedirect(reverse('forum_item:add'))
    # TODO uncomment
    # return HttpResponseRedirect(reverse('collection:forum'))
   

@login_required(login_url='/login/')
@csrf_exempt
def delete_post(request, id):
    post = Post.objects.get(id=id, author=request.user)
    post.delete()

    return HttpResponseRedirect(reverse('collection:forum'))

@login_required()
def add_comment(request: HttpRequest):
    if request.method=="POST":
        post = request.kwargs["id"],
        content = request.POST.get('content'),
        comment = ForumComment(
            post=post,
            commenter = request.user,
            date_created = datetime.now(),
            content = content,
            upvotes =0,
        )
    comment.save()
    return HttpResponse(serializers.serialize("json", [comment]), content_type ="application/json")

def add_reply(request: HttpRequest):
    if request.method=="POST":
        post = request.kwargs["id"],
        content = request.POST.get('content'),
        reply = Reply(
            post=post,
            commenter = request.user,
            date_created = datetime.now(),
            content = content,
            upvotes =0,
        )
    reply.save()
    return HttpResponse(serializers.serialize("json", [reply]), content_type ="application/json")