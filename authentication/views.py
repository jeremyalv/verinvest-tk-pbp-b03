from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from profile_page.models import Profile

@csrf_exempt
def login(request):
    username = request.POST.get("username")
    print(username)
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)
    
    if user is not None:
        if user.is_active:
            login(request, user)
            
            # Redirect to success page
            return JsonResponse({
                "status": True,
                "message": "Successfully logged in!",
                # TODO insert any data to be passed to flutter
                "username" : username,
                "password" : password
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Failed to login, account disabled.",
            }, status=401)
    else:
        return JsonResponse({
            "status": False,
            "message": "Failed to login, check your email or password",
            "username" : username,
            "password" : password
        }, status=401)

@csrf_exempt
def logout(request):
    try:
        logout(request)

        return JsonResponse({
            "status": True,
            "message": "Logout success",
        }, status=200)
    except:
        return JsonResponse({
            "status": False,
            "message": "Logout failed",
        }, status=401)

@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
   
        # TODO possible bug due to saving user as Profile object?
        if User.objects.get(username=username).exists():
            # If user has registered
            return JsonResponse({
                "status": False,
                "message": "User already exists",
            }, status=401)
        else:
            # If user has not registered
            user = User.objects.create_user(username=username, password=password)
            user.save()

            # TODO Create Profile instance
            # TODO add after creating flutter register page
            # Profile.objects.create(
            #         user = user,
            #         first_name = user.first_name,
            #         last_name = user.last_name,
            #         email = user.email,
            #         is_expert = user.is_expert,
            #         birth_date = None,
            #         occupation = None,
            #     )
            Profile.objects.create(
                user=user,
                first_name="Dummy",
                last_name="User",
                email="dummy@user.com",
                is_expert=False,
                birth_date=None,
                occupation=None,
            )

            return JsonResponse({
                "status": True,
                "username": user.username,
            }, status=200)
    else:
        return JsonResponse({
            "status": "error, not a POST request",
        }, status=401)
