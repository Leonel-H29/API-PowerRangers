from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import AutoField

# Create your models here.
class temporada(models.Model):
    id_temporada = AutoField(primary_key=True)
    numero_temporada = models.PositiveIntegerField(unique=True)
    nombre=models.CharField(max_length=50)
    descripcion=models.TextField(blank=True, null=True)
    foto=models.CharField(max_length=260)
    anio_estreno=models.PositiveIntegerField()
    cancion=models.CharField(max_length=260)
    basada_en=models.CharField(max_length=50)