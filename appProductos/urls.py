from django.contrib import admin
from django.urls import path, include
from . import views 


urlpatterns = [
    path('producto/', views.verProductos, name="productos"),
    path('producto/<str:id>', views.verProductos, name="producto"),
    path('carrito/<str:id>', views.agregar, name="carrito"),
    path('vercarrito/', views.verCarrito, name="ver_carrito"),
    path('eliminar/', views.eliminarItemCarrito, name="eliminar"),
    
]