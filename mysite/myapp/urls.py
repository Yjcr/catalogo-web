from django.urls import path
from . import views

urlpatterns = [
    path('', views.mostrar, name = 'home'), 
    path('registro', views.registro, name = 'register'),
    path('cerra_sesion', views.cerrar_sesion, name = 'logout'),
    path('inicio_sesion', views.inicio_sesion, name = 'login'),
    path('categorias/', views.categorias, name = 'categorys'),
    
]