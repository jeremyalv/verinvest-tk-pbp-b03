from django.urls import path
from edukasi_item.views import show_edukasi_item

app_name = 'edukasi_item'

urlpatterns = [
    path('', show_edukasi_item, name='show_edukasi_item'),
]
