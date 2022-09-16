from django.shortcuts import render
from appProductos.models import Producto

def bienvenido(request):

    return render(request, 'bienvenido.html');

def home(request):
    context={
        'productos': Producto.objects.all()
    }
    return render(request, 'home.html', context);

def contactenos(request):
    return render(request, 'contactenos.html');
