# rentscraper/urls.py

from django.urls import path
from rentscraper.views.views import scrape_killamreit_view
from .views.templeton_view import scrape_and_save_listings

urlpatterns = [
    path('killamreit/', scrape_killamreit_view, name='scrape_killamreit'),
    path('templeton/', scrape_and_save_listings, name='scrape_templeton'),

]
