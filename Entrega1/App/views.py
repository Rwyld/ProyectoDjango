from django.shortcuts import render
from .models import *

def index(request):
    plantas = Plantas.objects.all()
    maceteros = Maceteros.objects.all()
    libros = Libros.objects.all()

    vista = {"Plantas": plantas, "Maceteros": maceteros, "Libros": libros}
    return render(request, "app/index.html", vista)