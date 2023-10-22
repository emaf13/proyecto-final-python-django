from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

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
