from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Perfil

# UserCreationForm valida las dos contrasenas y aplica los validadores de Django.
class RegistroUsuarioForm(UserCreationForm):
    first_name = forms.CharField(label= 'Nombre',required=True)
    last_name = forms.CharField(label= 'Apellido', required=True)
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )


class PerfilForm(forms.ModelForm):
    
    class Meta:
        model = Perfil
        fields = ("biografia", "imagen_perfil")
        widgets = {
            "biografia": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            "imagen_perfil": forms.ClearableFileInput(
                attrs={"class": "form-control", "accept": "image/*"}
            ),
        }
