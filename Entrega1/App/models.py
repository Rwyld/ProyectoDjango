from http.client import PRECONDITION_FAILED
from django.db import models

# Create your models here.

class Plantas(models.Model):
    nombre = models.CharField("Nombre", max_length=30)
    tipo = models.CharField("Tipo", max_length=30)
    precio= models.FloatField("Precio $", max_length=10)
    LUGAR = (
        (1, "Interior"),
        (2, "Exterior"),
        (3, "Interior/Exterior")
    )
    lugar = models.PositiveSmallIntegerField("Espacio", choices=LUGAR)

class Maceteros(models.Model):
    TAMAÑO = (
        (1, "5cm"),
        (2, "10cm"),
        (3, "15cm"),
        (4, "20cm"),
        (5, "25cm"),
        (6, "30cm")
    )

    TIPO = (
        (1, "Plastico"),
        (2, "Madera"),
        (3, "Cemento")
    )

    tamaño = models.PositiveSmallIntegerField("Tamaño", choices=TAMAÑO)
    tipo = models.PositiveSmallIntegerField("Tipo", choices=TIPO)
    precio = models.FloatField("Precio $")

class Libros(models.Model):
    nombre = models.CharField("Nombre del Libro", max_length=30)
    precio = models.FloatField("Precio $")

class Usuario(models.Model):
    user = models.CharField("Usuario", max_length=30)
    email = models.CharField("Mail", max_length=100)
    contraseña = models.CharField("Contraseña", max_length=10)