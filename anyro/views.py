from django.shortcuts import render

def bienvenido(request):
    return render(request, 'bienvenido.html');

def home(request):
    return render(request, 'home.html');

def contactenos(request):
    return render(request, 'contactenos.html');

def registro(request):
    return render(request, 'registro.html');