from django.shortcuts import render, redirect, get_object_or_404
from .models import Videojuegos, Categorias
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.db.models import Q
from django.core.paginator import Paginator


def mostrar(request):
    query = request.GET.get("buscar")
    juegos = Videojuegos.objects.all()
    categorias = Categorias.objects.all()
    if query:
        juegos = Videogames.objects.filter(
            Q(name__icontains=query) or Q(description__icontains=query)
        ).distinct()
    paginador = Paginator(juegos, 9)
    page = request.GET.get("page")
    juegos = paginador.get_page(page)
    return {"game": juegos, "query": query, "categoria": categorias}
