from datetime import datetime
from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.decorators import login_required
from collection.models import Post
from edukasi_item.models import EdukasiComment
from edukasi_item.forms import EducationForm, CommentForm

def view_post(request, id):
    post_item = Post.objects.get(pk=id)
    comments = EdukasiComment.objects.filter(post=post_item)
    is_login = False

    if request.user.is_authenticated:
        is_login = True

    if request.method == "POST":
        cform = CommentForm(request.POST)
        if cform.is_valid():
            comment = EdukasiComment(
                post = post_item,
                commenter = request.user,
                date_created = datetime.now(),
                content = cform.cleaned_data["content"],
                upvotes = 0,
            )
            comment.save()
            return redirect(f'/{id}')
    else:
        cform = CommentForm()

    context = {
        'is_login':is_login,
        'post_item':post_item,
        'cform':cform,
        'comments':comments,
    }    
    
    return render(request, 'edukasi_item.html', context)

@login_required(login_url='landing_page:login')
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

@login_required(login_url='landing_page:login')
def delete_post(request, id):
    post = Post.objects.get(pk=id, author=request.user)
    post.delete()

    return HttpResponseRedirect(reverse('collection:education'))