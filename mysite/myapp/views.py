from django.shortcuts import render, redirect
from .models import Videogames, Category
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
# Create your views here.

def mostrar(request):
    juegos = Videogames.objects.all()
    return render(request, 'index.html', {'game':juegos} )
def categorias(request):
    categorias = Category.objects.all()
    # juegos = Videogames.GET.get('categoria')
    return render(request, 'base.html', {'categorias':categorias} )

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
            
            
   


             
