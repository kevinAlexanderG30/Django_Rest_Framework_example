from django.urls import path
from . import views

urlpatterns  = [
    path("", views.index, name="index"),
    path("obtener/", views.obtener_productos, name="obtener"),
    path("eliminar/", views.eliminar, name="eliminar")
]