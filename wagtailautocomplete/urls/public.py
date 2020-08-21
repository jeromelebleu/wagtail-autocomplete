from django.urls import path

from wagtailautocomplete.views import objects, search

urlpatterns = [
    path('objects/', objects),
    path('search/', search),
]
