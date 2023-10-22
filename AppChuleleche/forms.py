from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProveedorFormulario(forms.Form):
    nombre = forms.CharField()
    telefono = forms.CharField(required=False)
    correo = forms.EmailField(required=False)
    web = forms.URLField(required=False)
    descripcion = forms.CharField(required=False)
    hacen_envios = forms.BooleanField(required=False, initial=False)

class BuscarProveedorFormulario(forms.Form):
    nombre = forms.CharField()

class ClienteFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField(required=False)
    telefono = forms.CharField()
    correo = forms.EmailField()

class BuscarClienteFormulario(forms.Form):
    nombre = forms.CharField()

class PedidoFormulario(forms.Form):
    numero = forms.CharField()
    valor = forms.FloatField()
    fecha = forms.DateField()
    proveedor = forms.CharField()

class BuscarPedidoFormulario(forms.Form):
    fecha = forms.DateField()

class VentaFormulario(forms.Form):
    numero = forms.CharField()
    valor = forms.FloatField()
    fecha = forms.DateField()

class BuscarVentaFormulario(forms.Form):
    fecha = forms.DateField()

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="Usuario")
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Nombre", required=False)
    last_name = forms.CharField(label="Apellido", required=False)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
 
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}


class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Ingrese su email:")
    first_name = forms.CharField(label="Nombre", required=False)
    last_name = forms.CharField(label="Apellido", required=False)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']
