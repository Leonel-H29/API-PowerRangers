from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import AutoField

# Create your models here.
class temporada(models.Model):
    id_temporada = AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=300)
    foto=models.CharField(max_length=270)
    cancion=models.CharField(max_length=270)
    basada_en=models.CharField(max_length=50)