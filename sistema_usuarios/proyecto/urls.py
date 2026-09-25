"""
URL configuration for proyecto project.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),

    # URLs de nuestra aplicación usuarios
    path('', include('usuarios.urls')),
]
