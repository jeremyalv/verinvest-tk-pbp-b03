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
    post_item = Post.objects.filter(id=id).all()
    context = {
        'post_item':post_item
    }
    
    return render(request, 'edukasi_item.html', context)

# # @login_required
# # @csrf_exempt
def create_post(request):
    form = EducationForm()
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.post_type ='edukasi'
            post.author = request.user
            post.upvotes = 0
            post.viewers = 0
            post.comments_count = 0
            post.save()
            return redirect('collection:education')

    context = {'form':form}
    return render(request, 'create_education.html', context)

def post_json(request):
    post_all = Post.objects.all()
    return HttpResponse(serializers.serialize("json", post_all), content_type="application/json")

# # @login_required
# # @csrf_exempt
def delete_post(request, id):
    post = Post.objects.get(id=id, author=request.user)
    post.delete()

    return HttpResponseRedirect(reverse('collection:education'))

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