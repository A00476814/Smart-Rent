# rentscraper/urls.py

from django.urls import path
from .views import scrape_killamreit_view

urlpatterns = [
    path('killamreit/', scrape_killamreit_view, name='scrape_killamreit'),
]
