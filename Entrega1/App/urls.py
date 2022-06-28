from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= "index"),
    path('registro/', views.registro, name= "registro"),
    path('acerca/', views.acerca, name= "acerca"),
    path('plantas/', views.plantas, name= "plantas"),
    path('maceteros/', views.maceteros, name= "maceteros"),
    path('libros/', views.libros, name= "libros"),
]