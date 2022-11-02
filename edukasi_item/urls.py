from django.urls import path
from edukasi_item.views import view_post, create_post, delete_post, add_comment

app_name = 'edukasi_item'

urlpatterns = [
    path('<int:id>', view_post, name='view'),
    path('add/', create_post, name='add'),
    path('delete/<int:id>', delete_post, name='delete'),
    # path('comment/', add_comment, name='add_comment'),
]
