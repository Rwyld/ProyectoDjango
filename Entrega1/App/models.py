from distutils.command.upload import upload
from email.policy import default
from http.client import PRECONDITION_FAILED
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Inventario(models.Model):
    nombre = models.CharField("Nombre", max_length=30)
    tipo = models.CharField("Tipo", max_length=30)
    precio= models.FloatField("Precio $", max_length=10)
    imagen= models.ImageField(max_length=200, default='algo', upload_to='media')
    

class Usuario(models.Model):
    user = models.CharField("Usuario", max_length=30)
    email = models.CharField("Mail", max_length=100)
    contraseña = models.CharField("Contraseña", max_length=10)