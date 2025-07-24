# config/urls.py

# Django Imports
from django.contrib import admin
from django.urls import include, path

# List of main urls
urlpatterns = [
    path('admin/', admin.site.urls),

    # Apps
    path('sessions/', include('apps.sessions.urls')),
]
