from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User

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
        #Elimina los mensajes de ayuda
        help_texts = {k:"" for k in fields}


class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Ingrese su email:")
    first_name = forms.CharField(label="Nombre", required=False)
    last_name = forms.CharField(label="Apellido", required=False)
    password1 = forms.CharField(label='Por seguridad, Ingrese su contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña por favor', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']

class UserChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label=("Contraseña Actual"), widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label='Nueva Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(label='Repetir la Nueva contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

