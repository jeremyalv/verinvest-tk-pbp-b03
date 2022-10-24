from django.urls import path
from collection.views import (show_collection)

app_name = 'collection'

urlpatterns = [
    path('', show_collection, name='show_collection'),
]