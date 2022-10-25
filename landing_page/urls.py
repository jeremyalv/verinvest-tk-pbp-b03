from tkinter import N
from django.urls import path
from landing_page.views import (index, register, login_user, logout_user)


app_name = 'landing_page'

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
