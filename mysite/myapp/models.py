from django.db import models

class categoria(models.Model):
    categoria = models.CharField(max_length=100)
    
    def __str__(self):
        return self.categoria

class videojuego(models.Model):
    nombre = models.CharField(max_length=200)
    plataforma = models.CharField(max_length=250)
    precio = models.CharField(max_length=10)
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='galeria', null=False)
    
    def __str__(self):
        return self.nombre
    

