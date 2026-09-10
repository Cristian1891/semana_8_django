from django.db import models

class Posteo(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=75)
    contenido = models.TextField()
    fecha_creacion = models.DateField(auto_now_add=True)
    