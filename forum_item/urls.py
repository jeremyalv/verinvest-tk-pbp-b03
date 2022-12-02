from django.urls import path
from forum_item.views import (view_post, create_post, delete_post)

app_name = 'forum_item'

urlpatterns = [
    path('<int:id>/', view_post, name='view'),
    path('add/', create_post, name='add'),
    path('delete/<int:id>', delete_post, name='delete'),
]
