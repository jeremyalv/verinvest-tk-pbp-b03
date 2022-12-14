from django.urls import path
from landing_page.views import (index, register, login_user, logout_user,forto,show_forto_json,create_forto_modal, delete_forto_ajax)


app_name = 'landing_page'

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
     path('forto/',forto, name='forto'),
    path('landingpage/json/', show_forto_json, name='show-forto-json'),
    path('landingpage/add/', create_forto_modal, name='create-forto-modal'),
    path('landingpage/delete/<int:id>/', delete_forto_ajax, name='delete-forto-ajax'),
]
