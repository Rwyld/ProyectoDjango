from django.shortcuts import render
from .models import *

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