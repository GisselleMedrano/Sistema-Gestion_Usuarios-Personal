from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # Registro
    path(
        'registro/',
        views.registro,
        name='registro'
    ),

    # Login
    path(
        'login/',
        LoginView.as_view(template_name='usuarios/login.html'),
        name='login'
    ),

    # Bienvenida
    path(
        'bienvenida/',
        views.bienvenida,
        name='bienvenida'
    ),

    # Editar Perfil
    path(
        'editar-perfil/',
        views.editar_perfil,
        name='editar_perfil'
    ),

    # Eliminar Cuenta
    path(
        'eliminar-cuenta/', 
        views.eliminar_cuenta, 
        name='eliminar_cuenta'
    ),

    # Logout
    path(
        'logout/',
        LogoutView.as_view(),
        name='logout'
    ),
]