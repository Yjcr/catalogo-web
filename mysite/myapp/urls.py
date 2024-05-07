from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.mostrar, name = 'home'), 
=======
    path('juegos', views.mostrar, name = 'home'), 
>>>>>>> 591584c98dc4851f0c10419fb270c97b91a70d5b
    path('registro', views.registro, name = 'register'),
    path('cerra_sesion', views.cerrar_sesion, name = 'logout'),
    path('inicio_sesion', views.inicio_sesion, name = 'login')
]