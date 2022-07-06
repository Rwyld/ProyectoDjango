from django.contrib import admin
from .models import *
# Register your models here.

class InventarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'precio')


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'contraseña')


admin.site.register(Inventario, InventarioAdmin),
admin.site.register(Usuario, UsuarioAdmin),