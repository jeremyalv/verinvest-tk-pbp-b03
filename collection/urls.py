from django.urls import path
from collection.views import (show_collection, forum_archive, education_archive)

app_name = 'collection'

urlpatterns = [
    path('', show_collection, name='show_collection'),
    path('forum/', forum_archive, name='forum'),
    path('education/', education_archive, name='education'),
]