from django.contrib import admin
from .models import Videojuegos, Plataformas, Categorias, Desarrolladoras, Usuarios, Empleados, Clientes, Pagos, Detallesfactura, Facturas, Favoritos, Promociones, Reseñas, Ubicaciones 

# Register your models here.
admin.site.register(Videojuegos)
admin.site.register(Categorias)
admin.site.register(Plataformas)
admin.site.register(Desarrolladoras)
admin.site.register(Usuarios)
admin.site.register(Empleados)
admin.site.register(Clientes)
admin.site.register(Pagos)
admin.site.register(Detallesfactura)
admin.site.register(Facturas)
admin.site.register(Favoritos)
admin.site.register(Promociones)
admin.site.register(Reseñas)
admin.site.register(Ubicaciones)