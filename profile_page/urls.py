from django.urls import path
from profile_page.views import show_profile, edit_profile, get_profile_json, edit_firstname

app_name = 'profile_page'

urlpatterns = [
    path('', show_profile, name='show_profile'),
    path('edit/', edit_profile, name='edit_profile'),
    path('json/', get_profile_json, name='get_profile_json'),
    path('first_name/', edit_firstname, name='edit_firstname'),
]
