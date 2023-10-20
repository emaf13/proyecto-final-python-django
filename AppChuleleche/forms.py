from django import forms

class ProveedorFormulario(forms.Form):
    nombre = forms.CharField()
    telefono = forms.CharField()
    correo = forms.EmailField()
    hacen_envios = forms.BooleanField(required=False)

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

class BuscarPedidoFormulario(forms.Form):
    fecha = forms.DateField()

class VentaFormulario(forms.Form):
    numero = forms.CharField()
    valor = forms.FloatField()
    fecha = forms.DateField()

class BuscarVentaFormulario(forms.Form):
    fecha = forms.DateField()