from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from tunnelvision.views import index_view, monitor_view, remove_asset

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index_view, name="index"),
    path("monitor/", monitor_view, name="monitor"),
    path("remove_asset/<int:asset_id>/", remove_asset, name="remove_asset"),
]