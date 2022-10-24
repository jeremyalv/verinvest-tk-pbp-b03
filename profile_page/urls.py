from django.urls import path
from profile_page.views import show_profile

app_name = 'profile_page'

urlpatterns = [
    path('', show_profile, name='show_profile'),
]
