from django.urls import path
from profile_page.views import show_profile, edit_profile, get_profile_json
from profile_page.views import edit_firstname, edit_lastname, edit_email, edit_birthdate, edit_occupation

app_name = 'profile_page'

urlpatterns = [
    path('', show_profile, name='show_profile'),
    path('edit/', edit_profile, name='edit_profile'),
    path('json/', get_profile_json, name='get_profile_json'),
    path('first_name/', edit_firstname, name='edit_firstname'),
    path('last_name/', edit_lastname, name='edit_lastname'),
    path('email/', edit_email, name='edit_email'),
    path('birthdate/', edit_birthdate, name='edit_birthdate'),
    path('occupation/', edit_occupation, name='edit_occupation'),
]
