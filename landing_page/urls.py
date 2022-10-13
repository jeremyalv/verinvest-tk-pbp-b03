from django.urls import path
from landing_page.views import index

app_name = 'landing_page'

urlpatterns = [
    path('', index, name='index'),
]
