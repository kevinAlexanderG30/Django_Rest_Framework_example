from django.http import HttpResponse, JsonResponse
from app.models import Productos
from django.shortcuts import render, redirect

def index(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        precio = request.POST['precio']
        descripcion = request.POST['descripcion']
        producto = Productos(nombre=nombre, precio=precio, descripcion=descripcion)
        producto.save()
        return redirect('index')
    return render(request, "index.html")


def eliminar(request):
    print("entro")
    producto_id = request.POST.get('producto')
    #producto_id = request.POST.get('producto')
    producto = Productos.objects.get(id=producto_id)
    producto.delete()
    return redirect('index')


def obtener_productos(request):
    productos = Productos.objects.all()
    data = []
    for producto in productos:
        item = {'id': producto.id,
                'nombre': producto.nombre,
                'precio': producto.precio}
        data.append(item)
    return JsonResponse(data, safe=False)
# Create your views here.
