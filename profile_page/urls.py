from django.urls import path
from profile_page.views import main, show_watchlist, show_xml, show_json, show_xml_by_id, show_json_by_id

app_name = 'mywatchlist'

urlpatterns = [
    path('', main, name='show_main'),
]