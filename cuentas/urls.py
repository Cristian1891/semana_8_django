from django.urls import path
from cuentas import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("registro/", views.registro, name="registro"),
    path(
        "login/",
        LoginView.as_view(template_name="cuentas/login.html"),
        name="login",
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("perfil/", views.perfil, name="perfil"),
    path("perfil/editar/", views.editar_perfil, name="editar_perfil"),
]
