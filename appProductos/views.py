from multiprocessing import context
from django.shortcuts import render

# Create your views here.
from asyncio.windows_events import NULL
from django.shortcuts import render
from .models import Producto, Carrito

# Create your views here.
def verProductos(request, id=NULL):
    if not id:
        listaProductos = Producto.objects.all()
        context= {
            'productos': listaProductos,
        }
        return render(request, 'home.html', context)
    else:
        id= int(id)
        regProducto= Producto.objects.get(id=id)
        context ={
            'producto': regProducto,
        }
        return render(request, 'home.html', context)

def agregar (request, id= NULL):
    id = int(id)
    user = request.user
    regProducto = Producto.objects.get(id=id)
    existe= Carrito.objects.filter(cliente=user, producto = regProducto, estado ='carrito').exists()
    if existe:
        regCarrito = Carrito.objects.get(cliente = user, producto = regProducto, estado ='carrito')
        regCarrito.cantidad += 1
        regCarrito.save()
    else:
        regCarrito = Carrito(cliente = user, producto =regProducto, precio =regProducto.precio)
        regCarrito.save()   

    listaProductos = Producto.objects.all()
    context = {
            'productos': listaProductos,
        }
    return render(request, 'home.html', context)

def verCarrito(request):

    regUser= request.user
    carrito=Carrito.objects.filter(cliente=regUser, estado='carrito')
    print('=============')
    print(carrito)
    #recorrer elemento de carrito para calcular total

    listaCarrito=[]
    total=0
    context = {}
    for prod in carrito:
        unProducto={
            'cantidad':prod.cantidad,
            'icono':prod.producto.icono,
            'nombre':prod.producto.nombre,
            'valor':prod.producto.precio,
            'unidad':prod.producto.unidad,
            'total':int(prod.cantidad) * int(prod.producto.precio),
            'id':prod.id
        }

        listaCarrito.append(unProducto)
        total += unProducto['total']

        #ensamblar datos para la platilla

    context={
        'carrito': listaCarrito,
        'Subtotal': total,
        'iva': total * 0.19,
        'envio': 10000,
        'total': total * 1.19 + 10000
    }

    print('=============')
    print(context)

    return render(request, 'carrito.html', context)

def eliminarItemCarrito(request, id):
    #Consultar el reg
    regCarrito = Carrito.objects.get(id=id)
    regCarrito.estado = 'cancelado'
    #Guardar en BD
    regCarrito.save()
    #Desplegar el carrito
    return verCarrito(request)