from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, default='default description')
    
    def __str__(self):
        return self.name

class Videogames(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, default='default description')
    platform = models.CharField(max_length=250)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField()
    picture = models.ImageField(upload_to='galeria', null=False)
    video = models.FileField(upload_to='galeria', null=False, default='video')
    
    def __str__(self):
        return self.name
    

