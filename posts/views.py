from django.shortcuts import render, redirect
from posts.models import Posteo

# Create your views here.
def inicio(request):
    return render(request, "posts/inicio.html")


def lista_posts(request):
    # posts = [
    #     {"id": 1, "titulo": "Primer post", "autor": "Ana", "contenido": "Contenido del primer post."},
    #     {"id": 2, "titulo": "Segundo post", "autor": "Luis", "contenido": "Contenido del segundo post."},
    #     {"id": 3, "titulo": "Templates reutilizables", "autor": "Marta", "contenido": "Contenido del tercer post."},
    # ]
    
    posts = Posteo.objects.all()
    
    return render(request, "posts/lista_posts.html", {"posts": posts})

def detalle_post(request, post_id):
    # post = {
    #     "id": post_id,
    #     "titulo": f"Post número {post_id}",
    #     "autor": "Ana",
    #     "contenido": "Este es el contenido de ejemplo del post.",
    # }
    
    post = Posteo.objects.get(id=post_id)
    
    return render(request, "posts/detalle_post.html", {"post": post})

def contacto(request):
    return render(request, "posts/contacto.html")

def eliminar_post(request, post_id):

    post = Posteo.objects.get(id=post_id)
    post.delete()
    
    return redirect("lista_posts")

def crear_posts(request):
    
    print("De que tipo es la consulta:", request.method)
    print("GET:", request.GET)
    print("POST:", request.POST)
    
    if request.method == "POST":
        post = Posteo(titulo=request.POST.get('titulo'), autor=request.POST.get('autor'), contenido=request.POST.get('contenido'))
        post.save()
        
        return redirect("lista_posts")
    
    return render(request, "posts/crear_post.html", {})
