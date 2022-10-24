from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# @login_required
def show_collection(request):
    context = {}
    
    return render(request, 'collection.html', context)
