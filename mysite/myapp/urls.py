from django.urls import path
from . import views

urlpatterns = [
    path("", views.mostrar, name="Inicio"),
    path("registro", views.registro, name="register"),
    path("cerra_sesion", views.cerrar_sesion, name="logout"),
    path("inicio_sesion", views.inicio_sesion, name="login"),
    path(
        "categoria/<int:categoria_id>/",
        views.videojuegos_por_categorias,
        name="categories",
    ),
    path("detalles/<int:game_id>/", views.detalles, name="details"),
    path("search/",  views.search,  name="search"),
    path('create/', views.create, name="create"),
]
