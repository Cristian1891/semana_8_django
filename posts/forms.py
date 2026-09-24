from django import forms
from .models import Posteo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models import Perfil

# v1
# class CrearPosteo(forms.Form):
#     titulo = forms.CharField(max_length=200)
#     autor = forms.CharField(max_length=75)
#     contenido = forms.CharField(widget=forms.Textarea)



# v2
# class CrearPosteo(forms.ModelForm):
    
#     class Meta:
#         model = Posteo
#         # fields = ['titulo', 'autor']
#         fields = "__all__"


# class EditarPosteo(forms.ModelForm):
    
#     class Meta:
#         model = Posteo
#         # fields = ['titulo', 'autor']
#         fields = "__all__"
 
 
# class FormularioPosteo(forms.ModelForm):
    
#     class Meta:
#         model = Posteo
#         fields = "__all__"


# class CrearPosteo(FormularioPosteo): ...


# class EditarPosteo(FormularioPosteo): ...


class PosteoForm(forms.ModelForm):
    class Meta:
        model = Posteo
        fields = ("titulo", "autor", "contenido", "imagen")
        widgets = {
            "titulo": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Título del post",
                }
            ),
            "autor": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Nombre del autor",
                }
            ),
            "contenido": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 8,
                    "placeholder": "Contenido del post",
                }
            ),
            "imagen": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "accept": "image/*",
                }
            ),
        }
        


    def clean_titulo(self):
        titulo = self.cleaned_data["titulo"].strip()
        if len(titulo) < 5:
            raise forms.ValidationError(
                "El título debe tener al menos 5 caracteres.",
                code="titulo_corto",
            )
        return titulo

    def clean_contenido(self):
        contenido = self.cleaned_data["contenido"].strip()
        if len(contenido) < 20:
            raise forms.ValidationError(
                "El contenido debe tener al menos 20 caracteres.",
                code="contenido_corto",
            )
        return contenido
