from django.shortcuts import render

def show_profile(request):
    context = {
        'username' : request.user
    }

    return render(request, "profile.html", context)

def edit_profile(request):
    context = {
        'username' : request.user
    }
    return render(request, "modify.html", context)