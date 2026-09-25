from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from functools import wraps
from .models import Empleado
from .forms import EmpleadoForm

# Decorador personalizado para verificar permisos y enviar mensaje si no es admin
def admin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not (request.user.is_staff or request.user.is_superuser):
            messages.error(request, "Acceso denegado: No tienes permisos de administrador para ingresar a esta área.")
            return redirect('bienvenida')  # Redirige a la página de bienvenida
        return view_func(request, *args, **kwargs)
    return _wrapped_view

# 1. Menú principal del módulo de personal
@login_required
@admin_required
def index_personal(request):
    return render(request, 'personal/index.html')

# 2. READ: Listar todos los empleados
@login_required
@admin_required
def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'personal/lista_empleados.html', {'empleados': empleados})

# 3. CREATE: Registrar un nuevo empleado
@login_required
@admin_required
def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Empleado creado exitosamente.")
            return redirect('lista_empleados')
    else:
        form = EmpleadoForm()
    return render(request, 'personal/formulario_empleado.html', {'form': form, 'titulo': 'Registrar Empleado'})

# 4. READ (Detail): Ver información completa de un empleado
@login_required
@admin_required
def detalle_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    return render(request, 'personal/detalle_empleado.html', {'empleado': empleado})

# 5. UPDATE: Editar la información de un empleado
@login_required
@admin_required
def editar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            messages.success(request, "Datos del empleado actualizados.")
            return redirect('lista_empleados')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'personal/formulario_empleado.html', {'form': form, 'titulo': 'Modificar Empleado'})

# 6. DELETE: Confirmar y eliminar un empleado
@login_required
@admin_required
def eliminar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        empleado.delete()
        messages.success(request, "Empleado eliminado con éxito.")
        return redirect('lista_empleados')
    return render(request, 'personal/confirmar_eliminar.html', {'empleado': empleado})