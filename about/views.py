from django.shortcuts import render
from django.http import HttpRequest, HttpResponseBadRequest

# @login_required
def show_about(request):
    user_loggedin = False

    if request.user.is_authenticated:
        user_loggedin = True

    context = {
        'user_loggedin': user_loggedin
    }

    return render(request, 'about.html', context)
