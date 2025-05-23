"""
URL configuration for project3 project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('userapp.urls')),
    path('todo', include('todoapp.urls')),
]
