from django.shortcuts import render, redirect, get_object_or_404
from .models import (
    Videojuegos,
    Categorias,
    Desarrolladoras,
    Usuarios,
    Empleados,
    Clientes,
    Pagos,
    Detallesfactura,
    Facturas,
    Favoritos,
    Promociones,
    Reseñas,
    Ubicaciones,
)
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.db.models import Q
from django.http import HttpRequest
from .forms import crear_viedojuegos, crear_categorias, crear_desarrolladora
# Create your views here.


def mostrar(request):
    return render(
        request,
        "index.html",
    )

def detalles(request, game_id):
    juegos = get_object_or_404(Videojuegos, pk=game_id)
    return render(request, "details.html", {"game": juegos})

def videojuegos_por_categorias(request, categoria_id):
    categoria = Categorias.objects.get(idcategoria = categoria_id)
    videojuegos = Videojuegos.objects.filter(idcategoria = categoria)
    return render(request, 'categories.html', {'games': videojuegos})

def search(request: HttpRequest):
    return render(request, "search.html")

def create(request):
    if request.method == "GET":
     return render(request, "create.html", {'form_videojuegos':crear_viedojuegos,
                                            'form_categorias':crear_categorias,
                                            'form_desarrolladora':crear_desarrolladora})
    else:
     print(request.POST)
     return render(request, "create.html", {'form_videojuegos':crear_viedojuegos,
                                            'form_categorias':crear_categorias,
                                            'form_desarrolladora':crear_desarrolladora})

    
def registro(request):
    if request.method == "GET":
        return render(request, "sign_in.html", {"form": UserCreationForm})
    else:
        print(request.POST)
        if request.POST["password1"] == request.POST["password2"]:

            try:
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                user.save()
                login(request, user)
                return redirect("login")

            except IntegrityError:
                return render(
                    request,
                    "sign_in.html",
                    {
                        "form": UserCreationForm,
                        "ERROR": "El usuario ingresado ya existe",
                    },
                )
        else:
            return render(
                request,
                "sign_in.html",
                {"form": UserCreationForm, "ERROR": "Las contraseñas no coinciden"},
            )


def cerrar_sesion(request):
    logout(request)
    return redirect("Inicio") 

def inicio_sesion(request):
    if request.method == "GET":
        return render(request, "sign_up.html", {"form": AuthenticationForm})
    else:
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )

        if user is None:
            return render(
                request,
                "sign_up.html",
                {
                    "form": AuthenticationForm,
                    "ERROR": "Su Contraseña o usario son incorrectos",
                },
            )
        else:
            login(request, user)
            return redirect('Inicio')
            
        