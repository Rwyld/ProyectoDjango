import email
from sqlite3 import enable_shared_cache
from django.shortcuts import render
from .models import *
from App.forms import Registro

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

    if request.method == "POST":
        newuser = Registro(request.POST)

        if newuser.is_valid():
            info = newuser.cleaned_data
            regis_user = Usuario(user=info['user'], email=info['email'], contraseña=info['contraseña'])
        
            regis_user.save()
            return render(request, "app/2_registro2.html")

    else:
        newuser = Registro()

    return render(request, "app/2_registro.html", {"Registro": newuser})