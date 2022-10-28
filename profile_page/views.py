from django.shortcuts import render

# Create your views here.
def show_profile(request):
    context = {
        'username' : request.user,
    }

    return render(request, "profile.html", context)

