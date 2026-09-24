from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# class Posteo(models.Model):
#     titulo = models.CharField(max_length=200)
#     autor = models.CharField(max_length=75)
#     contenido = models.TextField()
#     fecha_creacion = models.DateField(auto_now_add=True)
    
    
class Posteo(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True, default="")
    autor = models.CharField(max_length=75)
    contenido = models.TextField()
    imagen = models.ImageField(
        upload_to="posts/%Y/%m/",
        null=True,
        blank=True,
        help_text="Opcional. Elegí una imagen JPG, PNG o WebP.",
    )
    fecha_creacion = models.DateField(auto_now_add=True)


    class Meta:
        ordering = ["-fecha_creacion"]

    def __str__(self):
        return self.titulo
    

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.titulo)[:200] or "post"
            candidato = base
            numero = 2
            # ¿Existe otro Posteo con este mismo slug?
            # pk=5
            while Posteo.objects.exclude(pk=self.pk).filter(
                slug=candidato
            ).exists():
                sufijo = f"-{numero}"
                candidato = f"{base[: 220 - len(sufijo)]}{sufijo}"
                numero += 1

            self.slug = candidato

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("detalle_post", kwargs={"slug": self.slug})