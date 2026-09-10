from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("posts/", views.lista_posts, name="lista_posts"),
    path("posts/crear/", views.crear_posts, name="crear_post"),
    path("posts/<int:post_id>/", views.detalle_post, name="detalle_post"),
    # path("posts/<int:post_id>/editar/", views.detalle_post, name="detalle_post"),
    path("posts/<int:post_id>/eliminar/", views.eliminar_post, name="eliminar_post"),
    path("contacto/", views.contacto, name="contacto"),
    
]

