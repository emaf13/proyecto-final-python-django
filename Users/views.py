from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from Users.forms import UserEditForm, UserRegisterForm


# Create your views here.
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
    return render(request, "Users/login.html", {"form":form})

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
      return render(request,"Users/register.html" ,  {"form":form})


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
    return render(request, "Users/edit.html", {"mi_form": miFormulario, "usuario": usuario})