from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# @login_required
def show_edukasi_item(request):
    context = {}
    
    return render(request, 'edukasi_item.html', context)
