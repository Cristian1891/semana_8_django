from django.contrib import admin
from .models import Posteo

# admin.site.register(Posteo)

@admin.register(Posteo)
class PosteoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "fecha_creacion")
    search_fields = ("titulo", "autor", "contenido")
    prepopulated_fields = {"slug": ("titulo",)}
