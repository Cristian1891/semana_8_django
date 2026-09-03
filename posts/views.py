from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, "posts/inicio.html")


def lista_posts(request):
    posts = [
        {"id": 1, "titulo": "Primer post", "autor": "Ana", "contenido": "Contenido del primer post."},
        {"id": 2, "titulo": "Segundo post", "autor": "Luis", "contenido": "Contenido del segundo post."},
        {"id": 3, "titulo": "Templates reutilizables", "autor": "Marta", "contenido": "Contenido del tercer post."},
    ]
    return render(request, "posts/lista_posts.html", {"posts": posts})

def detalle_post(request, post_id):
    post = {
        "id": post_id,
        "titulo": f"Post número {post_id}",
        "autor": "Ana",
        "contenido": "Este es el contenido de ejemplo del post.",
    }
    return render(request, "posts/detalle_post.html", {"post": post})

def contacto(request):
    return render(request, "posts/contacto.html")
