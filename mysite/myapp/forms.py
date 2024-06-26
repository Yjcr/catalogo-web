from django.forms import ModelForm
from .models import Videojuegos, Categorias, Desarrolladoras

class crear_categorias(ModelForm):
    class Meta:
        model = Categorias
        fields = ['nombrecategoria', 'descripcioncategoria']

class crear_viedojuegos(ModelForm):
    class Meta:
        model = Videojuegos
        fields = ['nombre', 'lanzamiento', 'descripcion', 
                  'plataforma', 'imagenjuego', 'iddesarrolladora',
                  'idcategoria'
                  ]
        
class crear_desarrolladora(ModelForm):
    class Meta:
        model = Desarrolladoras
        fields = ['nombredesarrolladora','descripciondes',
                  'sitioweb'
                  ]
