from django.contrib import admin
from django.urls import path, include
from . import views 


urlpatterns = [
    path('producto/', views.verProductos, name="productos"),
    path('producto/<str:id>', views.verProductos, name="producto"),
]