from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.db.models.fields import AutoField
from Temporadas.models import temporada

# Create your models here.
class capitulo(models.Model):
    id_capitulo = AutoField(primary_key=True)
    nombre=models.CharField(max_length=20)
    descripcion=models.CharField(max_length=150)
    id_temporada = models.ForeignKey(temporada, on_delete=DO_NOTHING)
