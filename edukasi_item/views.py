from datetime import datetime
from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.core import serializers
from collection.models import Post
from edukasi_item.models import EdukasiComment
from edukasi_item.forms import EducationForm, CommentForm

def view_post(request, id):
    post_item = Post.objects.filter(id=id)
    context = {
        'post_item':post_item
    }
    
    return render(request, 'edukasi_item.html', context)

# # @login_required
# # @csrf_exempt
# def create_post(request):
#     if request.method == 'POST':

#         title = request.POST.get('title')
#         content = request.POST.get('content')

#         Post.objects.create(
#             post_type='edukasi',
#             author=request.user,
#             title=title,
#             content=content,
#             upvotes=0,
#             viewers=0,
#             comments_count=0,
#         )

#         return HttpResponseRedirect(reverse('collection:forum'))
#     else:
#         form = EducationForm()
        
#     context = {
#         'form' : form,
#     }

#     return render(request, 'create_education.html', context)

# # @login_required
# # @csrf_exempt
# def delete_post(request, id):
#     post = Post.objects.get(id=id, author=request.user)
#     post.delete()

#     return HttpResponseRedirect(reverse('collection:education'))

# @login_required
# @csrf_exempt
def add_comment(request: HttpRequest):
    if request.method == "POST":
        post = request.kwargs["id"]
        content = request.POST.get('content')
        comment = EdukasiComment(
            post = post,
            commenter = request.user,
            date_created = datetime.now(),
            content = content,
            upvotes = 0,
        )
    comment.save()
    return HttpResponse(serializers.serialize("json", [comment]), content_type='application/json')

# def upvotes(request):
#     return

# def saved(request):
#     return

# from django.shortcuts import render
# from django.http import HttpResponse, HttpResponseRedirect
# from django.urls import reverse
# from django.contrib.auth.decorators import login_required
# from django.views.decorators.csrf import csrf_exempt

# from collection.models import Post
# # from forum_item.models import EdukasiComment
# # from forum_item.forms import EdukasiForm

# def view_post(request):
#     pass

# def create_post(request):
#     pass

# def delete_post(request):
#     pass

# @csrf_exempt
# def create_post(request):
#     if request.method == 'POST':

#         title = request.POST.get('title')
#         content = request.POST.get('content')

#         Post.objects.create(
#             post_type='forum',
#             author=request.user,
#             title=title,
#             content=content,
#             upvotes=0,
#             viewers=0,
#             comments_count=0,
#         )

#         return HttpResponseRedirect(reverse('collection:forum'))
#     else:
#         form = ForumForm()
        
#     context = {
#         'form' : form,
#     }

#     return render(request, 'create_forum.html', context)

# @csrf_exempt
# def delete_post(request, id):
#     post = Post.objects.get(id=id, author=request.user)
#     post.delete()

#     return HttpResponseRedirect(reverse('collection:forum'))