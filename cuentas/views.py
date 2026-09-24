from django.shortcuts import render, redirect
from cuentas.forms import RegistroUsuarioForm
from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
from .forms import RegistroUsuarioForm, PerfilForm
from .models import Perfil


def registro(request):
    if request.method == "POST":
        formulario = RegistroUsuarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("login")
    else:
        formulario = RegistroUsuarioForm()

    return render(request, "cuentas/registro.html", {"form": formulario})


@login_required
def perfil(request):
    # El perfil puede no existir todavia para un usuario nuevo.
    perfil, creado = Perfil.objects.get_or_create(user=request.user)
    return render(request, "cuentas/perfil.html", {"perfil": perfil})


@login_required
def editar_perfil(request):
    perfil, creado = Perfil.objects.get_or_create(user=request.user)
    if request.method == "POST":
        # FILES recibe el avatar; instance actualiza el perfil existente.
        formulario = PerfilForm(request.POST, request.FILES, instance=perfil)
        if formulario.is_valid():
            formulario.save()
            return redirect("perfil")
    else:
        formulario = PerfilForm(instance=perfil)

    return render(request, "cuentas/editar_perfil.html", {"form": formulario})
