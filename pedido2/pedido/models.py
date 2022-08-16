from unicodedata import name
from django.db import models

# Create your models here.

class Ensalada(models.Model):
    name    = models.CharField(max_length=100)
    priceM  = models.DecimalField(max_digits=4, decimal_places=2)
    priceL  = models.DecimalField(max_digits=4, decimal_places=2)
    pImage  = models.URLField() 

class Crema(models.Model):
    name    = models.CharField(max_length=100)
    priceM  = models.DecimalField(max_digits=4, decimal_places=2)
    priceL  = models.DecimalField(max_digits=4, decimal_places=2)
    cImage  = models.URLField() 

class Desayuno(models.Model):
    name    = models.CharField(max_length=100)
    priceM  = models.DecimalField(max_digits=4, decimal_places=2)
    priceL  = models.DecimalField(max_digits=4, decimal_places=2)
    dImage  = models.URLField() 

class Almuerzo(models.Model):
    name    = models.CharField(max_length=100)
    priceM  = models.DecimalField(max_digits=4, decimal_places=2)
    priceL  = models.DecimalField(max_digits=4, decimal_places=2)
    aImage  = models.URLField() 

class Formulario(models.Model):
    name = models.CharField('Nombres',max_length=100)
    asunto = models.CharField('Asunto', max_length=100)
    descripcion = models.TextField('Descripcion', max_length=1000)
    email = models.EmailField('Email')

    def __str__(self):
        return 'ASUNTO: ' + self.asunto 

# Formulario de preguntas 
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

class Receta(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion= models.TextField(max_length=1000)
    ingredintes= models.TextField(max_length=1000)
    rImage= models.URLField()