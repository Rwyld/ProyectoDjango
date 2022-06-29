from django.contrib import admin
from .models import *
# Register your models here.

class PlantasAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'lugar', 'precio')

class MaceterosAdmin(admin.ModelAdmin):
    list_display = ('tamaño', 'tipo', 'precio')

class LibrosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio')

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'contraseña')

admin.site.register(Plantas, PlantasAdmin),
admin.site.register(Maceteros, MaceterosAdmin),
admin.site.register(Libros, LibrosAdmin),
admin.site.register(Usuario, UsuarioAdmin),