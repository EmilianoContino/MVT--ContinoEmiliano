from unittest.util import _MAX_LENGTH
from django.db import models
# Create your models here.

class Familiar (models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_ingresado = models.DateField(null=True)
        
    def __str__(self):
        return f'{self.nombre} {self.apellido}'  #Para que se muestre el dato directo en la base  de datos.
    
    
