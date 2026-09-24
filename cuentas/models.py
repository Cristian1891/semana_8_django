from django.db import models
from django.contrib.auth.models import User


# El usuario de Django conserva las credenciales; Perfil guarda datos extra.
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biografia = models.TextField(blank=True)
    imagen_perfil = models.ImageField(
        upload_to="perfiles/",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"Perfil de {self.user.username}"
