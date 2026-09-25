from django.contrib import admin
from .models import Departamento, Cargo, Empleado

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'apellido', 'cargo', 'departamento', 'estado')
    search_fields = ('nombre', 'apellido', 'rut')
    list_filter = ('departamento', 'cargo', 'estado')
    ordering = ('apellido', 'nombre')