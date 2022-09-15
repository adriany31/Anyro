from django.contrib import admin
from django.urls import path
from . import views 
from django.urls import include
urlpatterns = [
  path('producto')
  path('producto/', views.verProductos, name="productos"),
  path('producto/<str:id>', views.verProductos, name="producto"),
]