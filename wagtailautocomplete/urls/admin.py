from django.urls import path

try:
    from wagtail.admin.auth import require_admin_access
except ImportError:
    from wagtail.admin.decorators import require_admin_access
from wagtailautocomplete.views import create, objects, search

urlpatterns = [
    path('create/', require_admin_access(create)),
    path('objects/', require_admin_access(objects)),
    path('search/', require_admin_access(search)),
]
