from django.shortcuts import render, redirect
from posts.models import Posteo
from posts.forms import CrearPosteo, EditarPosteo
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.urls import reverse_lazy

# Create your views here.
def inicio(request):
    return render(request, "posts/inicio.html")


# def lista_posts(request):
#     # posts = [
#     #     {"id": 1, "titulo": "Primer post", "autor": "Ana", "contenido": "Contenido del primer post."},
#     #     {"id": 2, "titulo": "Segundo post", "autor": "Luis", "contenido": "Contenido del segundo post."},
#     #     {"id": 3, "titulo": "Templates reutilizables", "autor": "Marta", "contenido": "Contenido del tercer post."},
#     # ]
    
#     posts = Posteo.objects.all()
    
#     return render(request, "posts/lista_posts.html", {"posts": posts})

# def detalle_post(request, post_id):
#     # post = {
#     #     "id": post_id,
#     #     "titulo": f"Post número {post_id}",
#     #     "autor": "Ana",
#     #     "contenido": "Este es el contenido de ejemplo del post.",
#     # }
    
#     post = Posteo.objects.get(id=post_id)
    
#     return render(request, "posts/detalle_post.html", {"post": post})

def contacto(request):
    return render(request, "posts/contacto.html")

# def eliminar_post(request, post_id):

#     post = Posteo.objects.get(id=post_id)
#     post.delete()
    
#     return redirect("lista_posts")

# def crear_posts(request):
    
#     if request.method == "POST":
        
#         formulario = CrearPosteo(request.POST)
        
#         if formulario.is_valid():
            
#             # v1
#             # info_limpia = formulario.cleaned_data
                
#             # post = Posteo(titulo=info_limpia.get('titulo'), autor=info_limpia.get('autor'), contenido=info_limpia.get('contenido'))
#             # post.save()
                
#             # v2
#             formulario.save()
            
#             return redirect("lista_posts")
#     else:
#         formulario = CrearPosteo()    
    
#     return render(request, "posts/crear_post.html", {"formulario": formulario})

# def editar_post(request, post_id):
    
#     posteo = Posteo.objects.get(id=post_id)
    
#     if request.method == "POST":
#         formulario = EditarPosteo(request.POST, instance=posteo)
#         if formulario.is_valid():
#             formulario.save()
#     else:
#         formulario = EditarPosteo(instance=posteo)
    
#     return render(request, "posts/editar_post.html", {"formulario": formulario, "post": posteo})

class VistaCrearPosteo(CreateView):
    model = Posteo
    template_name = "posts/crear_post.html"
    success_url = reverse_lazy('lista_posts')
    # fields = "__all__"
    form_class = CrearPosteo

class VistaEliminarPosteo(DeleteView):
    model = Posteo
    template_name = "posts/eliminar_post.html"
    success_url = reverse_lazy('lista_posts')

class VistaDetallePosteo(DetailView):
    model = Posteo
    template_name = "posts/detalle_post.html"

class VistaListarPosteo(ListView):
    model = Posteo
    template_name = "posts/lista_posts.html"
    context_object_name = "posts"

class VistaEditarPosteo(UpdateView):
    model = Posteo
    template_name = "posts/editar_post.html"
    success_url = reverse_lazy('lista_posts')
    fields = "__all__"
