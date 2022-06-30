from django.shortcuts import render

from App.forms import Registro
from .models import *
from django.http import HttpResponse


def index(request):
    return render(request, "app/index.html")

def acerca(request):
    return render(request, "app/0_acerca.html")

def libros(request):
    return render(request, "app/1_libros.html")

def maceteros(request):
    return render(request, "app/1_maceteros.html")

def plantas(request):
    return render(request, "app/1_plantas.html")

def registro(request):

    if request.method == 'POST':
        newuser = Registro(request.POST)

        if newuser.is_valid():
            info = newuser.cleaned_data
            usuario = Usuario(user=info['user'], email=info['email'], contraseña=info['contraseña'])
            usuario.save()

            return render(request, "app/2_registro2.html")
    
    else:
        newuser = Registro()

    return render(request, "app/2_registro.html", {"Newuser":newuser})

def busqueda(request):
    
    if request.GET["producto"]:
        #mensaje="articulo buscado: %r" %request.GET["producto"]
        prd=request.GET["producto"]

        plant=Plantas.objects.filter(nombre__icontains=prd)
        #books=Libros.objects.filter(nombre__icontains=prd)
        #articulos={"plant": plant, "books": books}

        return render(request, "app/busqueda.html", {"plant":plant, "query": prd})

    else:
        mensaje="no has introducido nada"

    return HttpResponse (mensaje)