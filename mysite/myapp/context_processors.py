from django.shortcuts import render, redirect, get_object_or_404
from .models import Videogames, Category
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.db.models import Q

def mostrar(request):
    query = request.GET.get("buscar")
    juegos = Videogames.objects.all()  
    categorias = Category.objects.all()
    print(query)
    if query:
         juegos = Videogames.objects.filter(
            Q(name__icontains = query) or 
            Q(description__icontains = query)
         ).distinct()
         
         print(juegos)
    return {'game':juegos, 
            'categoria':categorias}

