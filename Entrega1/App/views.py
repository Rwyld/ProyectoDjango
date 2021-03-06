from django.shortcuts import render

from App.forms import Registro
from .models import *
from django.http import HttpResponse



def index(request):
    inventarios=Inventario.objects.all()

    return render(request, "app/index.html", {"inventarios":inventarios})

def acerca(request):
    inventarios=Inventario.objects.all()
    return render(request, "app/0_acerca.html", {"inventarios":inventarios})

def libros(request):
    inventarios=Inventario.objects.all()
    return render(request, "app/1_libros.html", {"inventarios":inventarios})

def maceteros(request):
    inventarios=Inventario.objects.all()
    return render(request, "app/1_maceteros.html", {"inventarios":inventarios})

def plantas(request):
    inventarios=Inventario.objects.all()
    return render(request, "app/1_plantas.html", {"inventarios":inventarios})

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