from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = [
            'rut', 
            'nombre', 
            'apellido', 
            'email', 
            'telefono', 
            'fecha_ingreso', 
            'cargo', 
            'departamento', 
            'estado'
        ]
        labels = {
            'rut': 'RUT / Identificador',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'email': 'Correo electrónico',
            'telefono': 'Teléfono',
            'fecha_ingreso': 'Fecha de ingreso',
            'cargo': 'Cargo',
            'departamento': 'Departamento',
            'estado': 'Estado',
        }
        widgets = {
            'fecha_ingreso': forms.DateInput(attrs={'type': 'date'}),
        }