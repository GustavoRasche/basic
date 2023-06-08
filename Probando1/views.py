from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def ventas(request):
    return render(request, 'ventas.html')

def catalogo(request):
    return render(request, 'catalogo.html')