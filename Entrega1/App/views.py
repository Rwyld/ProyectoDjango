from django.shortcuts import render
from .models import *

def index(request):
    return render(request, "app/index.html")

def registro(request):
    return render(request, "app/base.html")

def libros(request):
    return render(request, "app/1_libros.html")