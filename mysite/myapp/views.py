from django.shortcuts import render, redirect, get_object_or_404
from .models import Videogames, Category
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.db.models import Q
# Create your views here.

def mostrar(request):
        # query = request.GET.get("buscar")
        # juegos = Videogames.objects.all()  
        # categorias = Category.objects.all()
        # if query:
        #      juegos = Videogames.objects.filter(
        #         Q(name__icontains = query) or 
        #         Q(description__icontains = query)
        #      ).distinct()
        return render(request, 'index.html',)

def detalles(request, game_id):
    juegos = get_object_or_404(Videogames, pk=game_id)
    
    return render(request, 'details.html', {'games': juegos})
    
    
def videojuegos_por_categorias(request, categoria_id):
    # print(Category.objects.get(id=categoria_id))
    # categoria = get_object_or_404(Category, categoria_id)
    categoria = Category.objects.get(id=categoria_id)
    # print(Category.objects.get(id=categoria_id))
    videojuegos = Videogames.objects.filter(category=categoria)
    return render(request, 'categorys.html', {'games': videojuegos} )

    
def registro(request):
    if request.method == 'GET':
        return render(request, 'sign_in.html', {'form':UserCreationForm})
    else:
        print(request.POST)
        if request.POST['password1'] == request.POST['password2']:
            
         try:
             user = User.objects.create_user(username = request.POST['username'],
                                             password = request.POST['password1'])
             user.save()
             login(request, user)
             return redirect('login')
         
         except IntegrityError:
               return render(request, 'sign_in.html', {'form':UserCreationForm,
                                                       'error':'tu usuario ya existe'})
        else:
               return render(request, 'sign_in.html', {'form':UserCreationForm,
                                                       'error': 'la contraseña no coinciden'})
               
def cerrar_sesion(request):
    logout(request)
    return redirect('home')

def inicio_sesion(request):
    if request.method == 'GET':
        return render(request, 'sign_up.html', {'form':AuthenticationForm})
    else:
        user = authenticate(request, username = request.POST['username'], 
                                     password = request.POST['password'])
    
        if user is None:
             return render(request, 'sign_up.html', {'form':AuthenticationForm,
                                                    'error':'tu clave o usario es incorrecta'})  
        else:
            login(request, user)
            return redirect('home')
            
            
   


             
