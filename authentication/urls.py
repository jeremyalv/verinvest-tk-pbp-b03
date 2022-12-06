from django.urls import path, include
from authentication.views import login, logout, register

app_name = 'collection'

urlpatterns = [
    path('flutter-login/', login, name='flutter-login'),
    path('flutter-logout/', logout, name='flutter-logout'),
    path('flutter-register/', register, name='flutter-register'),
]