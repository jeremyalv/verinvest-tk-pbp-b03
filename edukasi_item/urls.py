from django.urls import path
from edukasi_item.views import view_post

app_name = 'edukasi_item'

urlpatterns = [
    path('<int:id>', view_post, name='view'),
#     path('add/', create_post, name='add'),
#     path('delete/<int:id>', delete_post, name='delete'),
]