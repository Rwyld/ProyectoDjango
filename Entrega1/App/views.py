from django.shortcuts import render
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
    return render(request, "app/2_registro.html")

def busqueda(request):
    
    if request.GET["producto"]:
        mensaje="articulo buscado: %r" %request.GET["producto"]
        prd=request.GET["producto"]

        maceta=Maceteros.objects.filter(nombre__icontains=prd)
        plant=Plantas.objects.filter(nombre__icontains=prd)
        books=Libros.objects.filter(nombre__icontains=prd)
        articulos={"maceta":maceta, "plant": plant, "books": books}

        return render(request, "app/busqueda.html", {"articulos":articulos, "query": prd})

    else:
        mensaje="no has introducido nada"

    return HttpResponse (mensaje)