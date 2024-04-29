from django.shortcuts import render
from .models import videojuego
from django.shortcuts import render
# Create your views here.
def mostrar(request):
    juegos = videojuego.objects.all()
    return render(request, 'index.html', {'game':juegos} )
