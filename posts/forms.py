from django import forms
from posts.models import Posteo

# v1
# class CrearPosteo(forms.Form):
#     titulo = forms.CharField(max_length=200)
#     autor = forms.CharField(max_length=75)
#     contenido = forms.CharField(widget=forms.Textarea)


# v2
class CrearPosteo(forms.ModelForm):
    
    class Meta:
        model = Posteo
        # fields = ['titulo', 'autor']
        fields = "__all__"


class EditarPosteo(forms.ModelForm):
    
    class Meta:
        model = Posteo
        # fields = ['titulo', 'autor']
        fields = "__all__"
 
 
# class FormularioPosteo(forms.ModelForm):
    
#     class Meta:
#         model = Posteo
#         fields = "__all__"


# class CrearPosteo(FormularioPosteo): ...


# class EditarPosteo(FormularioPosteo): ...