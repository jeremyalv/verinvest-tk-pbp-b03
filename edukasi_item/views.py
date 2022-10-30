from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from collection.models import Post
# from forum_item.models import EdukasiComment
# from forum_item.forms import EdukasiForm

def view_post(request):
    pass

def create_post(request):
    pass

def delete_post(request):
    pass

