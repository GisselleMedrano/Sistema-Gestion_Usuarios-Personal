# render permite cargar un archivo HTML.
# redirect permite enviar al usuario hacia otra página.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Importamos nuestro formulario.
from .forms import (
    RegistroUsuarioForm,
    EditarUsuarioForm,
)

# Vista responsable del registro.
def registro(request):
    # Comprobamos si el navegador está enviando información mediante POST.
    if request.method == 'POST':
        # Creamos un formulario utilizando la información recibida.
        form = RegistroUsuarioForm(request.POST)
        
        # Verificamos que los datos sean válidos.
        if form.is_valid():
            # Guardamos el usuario. Django se encargará de almacenarlo en la BD.
            form.save()
            
            # Después del registro enviamos al usuario a la página de login.
            return redirect('login')
    else:
        # Si solamente estamos entrando a la página (método GET), creamos un formulario vacío.
        form = RegistroUsuarioForm()

    # Mostramos el archivo HTML.
    return render(
        request,
        'usuarios/registro.html',
        {
            'form': form
        }
    )

# login_required significa que solamente usuarios autenticados pueden acceder.
@login_required
def bienvenida(request):
    return render(
        request,
        'usuarios/bienvenida.html',
        {
            'fecha_registro': request.user.date_joined
        }
    )
#--------------------------------------------------------------------------------------------
@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = EditarUsuarioForm(
            request.POST,
            instance=request.user
        )
        if form.is_valid():
            form.save()
            return redirect('bienvenida')
    else:
        form = EditarUsuarioForm(instance=request.user)
    
    # Este return DEBE estar alineado al mismo nivel del 'if' inicial
    return render(
        request,
        'usuarios/editar_perfil.html',
        {
            'form': form
        }
    )

@login_required
def eliminar_cuenta(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        return redirect('login')
    
    return render(request, 'usuarios/eliminar_cuenta.html')