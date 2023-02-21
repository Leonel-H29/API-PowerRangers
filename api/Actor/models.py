from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.db.models.fields import AutoField
from Temporadas.models import temporada

# Create your models here.
class actor(models.Model):
    id_actor= AutoField(primary_key=True)
    nombre_actor=models.CharField(max_length=80)
    nombre_artistico=models.CharField(max_length=80, blank=True, null=True)
    foto=models.CharField(max_length=260)
    biografia=models.CharField(max_length=260)


class personaje(models.Model):
    id_personaje= AutoField(primary_key=True)
    nombre_personaje=models.CharField(max_length=80)
    descripcion=models.TextField(blank=True, null=True)
    foto=models.CharField(max_length=260)
    id_actor= models.ForeignKey(actor, on_delete=DO_NOTHING)
    #temporada=models.ManyToManyField(temporada, related_name='aparecen')
    
class aparecen(models.Model):
    id_aparicion = AutoField(primary_key=True)
    id_personaje= models.ForeignKey(personaje, on_delete=CASCADE)
    id_temporada = models.ForeignKey(temporada, on_delete=CASCADE)
    rol=models.CharField(max_length=10)
