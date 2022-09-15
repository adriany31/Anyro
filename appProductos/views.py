from django.shortcuts import render

# Create your views here.
from asyncio.windows_events import NULL
from django.shortcuts import render
from .models import Producto

# Create your views here.
def verProductos(request, id=NULL):
    if not id:
        listaProductos = Producto.objects.all()
        context= {
            'productos': listaProductos,
        }
        return render(request, 'home.hmtl', context)
    else:
        id= int(id)
        regProducto= Producto.objects.get(id=id)
        context ={
            'producto': regProducto,
        }
        return render(request, 'home.hmtl', context)

