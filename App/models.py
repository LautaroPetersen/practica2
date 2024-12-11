from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=40)
class Subcategoria(models.Model):
    nombre = models.CharField(max_length=40)
class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    color = models.CharField(max_length=30)
    talle = models.CharField(max_length=5) 