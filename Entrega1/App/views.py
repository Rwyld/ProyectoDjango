from django.shortcuts import render

from App.forms import Registro
from .models import *
from django.http import HttpResponse



def index(request):
    items=Inventario.objects.all()

    return render(request, "app/index.html", {"items":items})

def acerca(request):
    return render(request, "app/0_acerca.html")

def libros(request):
    items=Inventario.objects.all()
    return render(request, "app/1_libros.html", {"items":items})

def maceteros(request):
    items=Inventario.objects.all()
    return render(request, "app/1_maceteros.html", {"items":items})

def plantas(request):
    items=Inventario.objects.all()
    return render(request, "app/1_plantas.html", {"items":items})

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

        inventarios=Inventario.objects.filter(nombre__icontains=prd)
       

        return render(request, "app/busqueda.html", {"inventarios":inventarios, "query": prd})
    
    else:
        mensaje="no has introducido nada"

    return HttpResponse (mensaje)