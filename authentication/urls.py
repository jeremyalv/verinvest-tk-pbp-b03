from django.urls import path, include
from authentication.views import login, logout, register

app_name = 'collection'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
]