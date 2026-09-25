from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_personal, name='index_personal'),
    path('empleados/', views.lista_empleados, name='lista_empleados'),
    path('empleados/crear/', views.crear_empleado, name='crear_empleado'),
    path('empleados/<int:pk>/', views.detalle_empleado, name='detalle_empleado'),
    path('empleados/<int:pk>/editar/', views.editar_empleado, name='editar_empleado'),
    path('empleados/<int:pk>/eliminar/', views.eliminar_empleado, name='eliminar_empleado'),
]