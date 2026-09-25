# Importamos el sistema de formularios de Django.
from django import forms

# Importamos el validador para expresiones regulares
from django.core.validators import RegexValidator

# Django ya incorpora un formulario diseñado especialmente para crear usuarios.
from django.contrib.auth.forms import UserCreationForm

# Importamos el modelo de usuario incorporado por Django
from django.contrib.auth.models import User


# Validador para asegurar que solo contenga letras (incluyendo tildes, ñ y espacios)
solo_letras = RegexValidator(
    r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$',
    'Este campo solo puede contener letras y espacios.'
)


# Creamos nuestro formulario de registro
class RegistroUsuarioForm(UserCreationForm):

    # Sobrescribimos el nombre para que sea obligatorio y acepte solo letras
    first_name = forms.CharField(
        required=True,
        label='Nombre',
        validators=[solo_letras]
    )

    # Sobrescribimos el apellido para que sea obligatorio y acepte solo letras
    last_name = forms.CharField(
        required=True,
        label='Apellido',
        validators=[solo_letras]
    )

    # Agregamos el correo electrónico porque queremos solicitarlo obligatoriamente.
    email = forms.EmailField(
        required=True,
        label='Correo electrónico'
    )

    class Meta:
        # Indicamos que este formulario trabaja con el modelo User.
        model = User
        
        # Definimos los campos que aparecerán en nuestro formulario.
        # Nota: UserCreationForm ya maneja las contraseñas internamente.
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]


# Formulario para editar datos del usuario.
class EditarUsuarioForm(forms.ModelForm):

    first_name = forms.CharField(
        required=True,
        label='Nombre',
        validators=[solo_letras]
    )

    last_name = forms.CharField(
        required=True,
        label='Apellido',
        validators=[solo_letras]
    )

    email = forms.EmailField(
        required=True,
        label='Correo electrónico'
    )

    class Meta:
        # Trabajamos con User.
        model = User
        # Solamente permitiremos modificar estos campos.
        fields = [
            'first_name',
            'last_name',
            'email',
        ]