from django.contrib import admin
from .models import Videogames, Category

# Register your models here.
admin.site.register(Videogames)
admin.site.register(Category)