from unicodedata import name
from django.db import models

# Create your models here.

class Ensalada(models.Model):
    name    = models.CharField(max_length=100)
    priceM  = models.DecimalField(max_digits=4, decimal_places=2)
    priceL  = models.DecimalField(max_digits=4, decimal_places=2)
    pImage  = models.URLField() 