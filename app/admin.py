from django.contrib import admin
from app.models import Productos

@admin.register(Productos)

class AdminProductos(admin.ModelAdmin):
    list_display = ['id', 'nombre']
