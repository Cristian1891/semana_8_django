from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("contacto/", views.contacto, name="contacto"),
    
    # sin vbc
    # path("posts/", views.lista_posts, name="lista_posts"),
    # path("posts/crear/", views.crear_posts, name="crear_post"),
    # path("posts/<int:post_id>/", views.detalle_post, name="detalle_post"),
    # path("posts/<int:post_id>/editar/", views.editar_post, name="editar_post"),
    # path("posts/<int:post_id>/eliminar/", views.eliminar_post, name="eliminar_post"),
    
    # con vbc
    path("posts/", views.VistaListarPosteo.as_view(), name="lista_posts"),
    path("posts/crear/", views.VistaCrearPosteo.as_view(), name="crear_post"),
    path(
        "posts/<slug:slug>/",
        views.VistaDetallePosteo.as_view(),
        name="detalle_post",
    ),
    path(
        "posts/<slug:slug>/editar/",
        views.VistaEditarPosteo.as_view(),
        name="editar_post",
    ),
    path(
        "posts/<slug:slug>/eliminar/",
        views.VistaEliminarPosteo.as_view(),
        name="eliminar_post",
    ),

    # path("posts/crear/", views.VistaCrearPosteo.as_view(), name="crear_post"),
    # path("posts/<int:pk>/", views.VistaDetallePosteo.as_view(), name="detalle_post"),
    # path("posts/<int:pk>/editar/", views.VistaEditarPosteo.as_view(), name="editar_post"),
    # path("posts/<int:pk>/eliminar/", views.VistaEliminarPosteo.as_view(), name="eliminar_post"),
    
]

