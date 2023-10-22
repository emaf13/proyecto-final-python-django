from django.shortcuts import render
from AppChuleleche.models import Proveedor, Cliente, Pedido, Venta
from AppChuleleche.forms import *
from django.views.generic import ListView

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            clave = form.cleaned_data.get("password")
            nombre_usuario = authenticate(username=usuario, password=clave)
            if usuario is not None:
                login (request, nombre_usuario)
                return render(request, "AppChuleleche/index.html", {"mensaje":f"Has iniciado sesión. Bienvenido {usuario}"})
            else:
                return render(request, "AppChuleleche/index.html", {"mensaje":"Error, datos incorrectos"})
        else:
            return render(request, "AppChuleleche/index.html", {"mensaje":"Error, formulario inválido"})
    form = AuthenticationForm()
    return render(request, "AppChuleleche/login.html", {"form":form})

def register(request):
      if request.method == 'POST':
            ###form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppChuleleche/index.html" ,  {"mensaje":"Usuario Creado :)"})
      else:
            ###form = UserCreationForm()       
            form = UserRegisterForm()     
      return render(request,"AppChuleleche/register.html" ,  {"form":form})




@login_required
def editProfile(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
            usuario.save()
            return render(request, "AppChuleleche/index.html", {"mensaje":f"Usuario {usuario} actualizado correctamente"})
    else:
        miFormulario = UserEditForm(initial={'email': usuario.email, 'first_name': usuario.first_name, 'last_name': usuario.last_name})
    return render(request, "AppChuleleche/edit_user.html", {"mi_form": miFormulario, "usuario": usuario})


class ProveedorListView(LoginRequiredMixin, ListView):
    model = Proveedor
    template_name = "AppChuleleche/proveedores_resultados_cbv.html"

# Create your views here.
def inicio(request):
    return render(request, "AppChuleleche/index.html")

@login_required
def proveedores(request):
    return render(request, "AppChuleleche/proveedores.html")

def pedidos(request):
    return render(request, "AppChuleleche/pedidos.html")

def clientes(request):
    return render(request, "AppChuleleche/clientes.html")

def ventas(request):
    return render(request, "AppChuleleche/ventas.html")

# def formulario_proveedores(request):
#     return render(request, "AppChuleleche/proveedores_formulario.html")

 
def alta_proveedores(request):
    if request.method == "POST":
        miFormulario = ProveedorFormulario(request.POST) # Creo una instancia de ProveedorFormulario con la informacion que llega del html 
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            prov = Proveedor(nombre=info["nombre"], telefono=info["telefono"], correo=info["correo"], hacen_envios=info["hacen_envios"])
            prov.save()
            return render(request, "AppChuleleche/index.html")
    else:
        miFormulario = ProveedorFormulario()
 
    return render(request, "AppChuleleche/proveedores_alta.html", {"miFormulario": miFormulario})

def buscar_proveedores(request):
    if request.method == "POST":
        miFormulario = BuscarProveedorFormulario(request.POST)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            provs = Proveedor.objects.filter(nombre__icontains=info["nombre"])
            return render(request, "AppChuleleche/proveedores_resultados.html", {"proveedores": provs})
    else:
        miFormulario = BuscarProveedorFormulario()
 
    return render(request, "AppChuleleche/proveedores_buscar.html", {"miFormulario": miFormulario})

def alta_clientes(request):
    if request.method == "POST":
        miFormulario = ClienteFormulario(request.POST)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            cliente = Cliente(nombre=info["nombre"], telefono=info["telefono"], correo=info["correo"], apellido=info["apellido"])
            cliente.save()
            return render(request, "AppChuleleche/index.html")
    else:
        miFormulario = ClienteFormulario()
 
    return render(request, "AppChuleleche/clientes_alta.html", {"miFormulario": miFormulario})

def buscar_clientes(request):
    if request.method == "POST":
        miFormulario = BuscarClienteFormulario(request.POST)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            cliente = Cliente.objects.filter(nombre__icontains=info["nombre"])
            return render(request, "AppChuleleche/clientes_resultados.html", {"clientes": cliente})
    else:
        miFormulario = BuscarClienteFormulario()
 
    return render(request, "AppChuleleche/clientes_buscar.html", {"miFormulario": miFormulario})

def alta_pedidos(request):
    if request.method == "POST":
        miFormulario = PedidoFormulario(request.POST) 
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            ped = Pedido(numero=info["numero"], valor=info["valor"], fecha=info["fecha"])
            ped.save()
            return render(request, "AppChuleleche/index.html")
    else:
        miFormulario = PedidoFormulario()
 
    return render(request, "AppChuleleche/pedidos_alta.html", {"miFormulario": miFormulario})

def buscar_pedidos(request):
    if request.method == "POST":
        miFormulario = BuscarPedidoFormulario(request.POST)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            pedidos = Pedido.objects.filter(fecha__icontains=info["fecha"])
            return render(request, "AppChuleleche/pedidos_resultados.html", {"pedidos": pedidos})
    else:
        miFormulario = BuscarPedidoFormulario()
 
    return render(request, "AppChuleleche/pedidos_buscar.html", {"miFormulario": miFormulario})

def alta_ventas(request):
    if request.method == "POST":
        miFormulario = VentaFormulario(request.POST) 
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            ven = Venta(numero=info["numero"], valor=info["valor"], fecha=info["fecha"])
            ven.save()
            return render(request, "AppChuleleche/index.html")
    else:
        miFormulario = VentaFormulario()
 
    return render(request, "AppChuleleche/ventas_alta.html", {"miFormulario": miFormulario})

def buscar_ventas(request):
    if request.method == "POST":
        miFormulario = BuscarVentaFormulario(request.POST)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            ventas = Venta.objects.filter(fecha__icontains=info["fecha"])
            return render(request, "AppChuleleche/ventas_resultados.html", {"ventas": ventas})
    else:
        miFormulario = BuscarVentaFormulario()
 
    return render(request, "AppChuleleche/ventas_buscar.html", {"miFormulario": miFormulario})