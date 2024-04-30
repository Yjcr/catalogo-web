from django.shortcuts import render, redirect
from .models import videojuego
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
# Create your views here.

def mostrar(request):
    juegos = videojuego.objects.all()
    return render(request, 'index.html', {'game':juegos} )

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
            
                # return render(request, 'index_admin.html', {'form':juegos})
            
            
   


             
