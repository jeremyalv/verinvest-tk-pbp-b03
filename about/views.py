from django.shortcuts import render
from django.http import HttpRequest, HttpResponseBadRequest

# @login_required
def show_about(request):
    return render(request, 'about.html')
