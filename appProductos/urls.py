from django.contrib import admin
from django.urls import path
from . import views 
from django.urls import include
urlpatterns = [
<<<<<<< HEAD
  path('producto')
=======
  path('producto/', views.verProductos, name="productos"),
  path('producto/<str:id>', views.verProductos, name="producto"),
>>>>>>> f0fd54723e6776c06eaa751bd8fe5c208a0b70e4
]