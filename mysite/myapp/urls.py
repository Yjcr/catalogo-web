from django.urls import path
from . import views

urlpatterns = [
    path('juegos', views.mostrar),
]