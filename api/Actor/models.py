from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.db.models.fields import AutoField
from Temporadas.models import temporada

# Create your models here.
class actor(models.Model):
    id_actor= AutoField(primary_key=True)
    nombre_actor=models.CharField(max_length=80, unique=True)
    nombre_artistico=models.CharField(max_length=80, blank=True, null=True)
    foto=models.CharField(max_length=260)
    biografia=models.CharField(max_length=260)
    
    def __str__(self):
        return str(self.id_actor)  + self.nombre_actor
    
    class Meta :
        db_table='actor'
        verbose_name='actor'
        verbose_name_plural='actores'
        ordering = ['nombre_actor']


class personaje(models.Model):
    id_personaje= AutoField(primary_key=True)
    nombre_personaje=models.CharField(max_length=80)
    descripcion=models.TextField(blank=True, null=True)
    foto=models.CharField(max_length=260)
    id_actor= models.ForeignKey(actor, on_delete=DO_NOTHING, db_column='id_actor')
    #temporada=models.ManyToManyField(temporada, related_name='aparecen')
    
    def __str__(self):
        return str(self.id_personaje) + ")- " + self.nombre + "-- " + str(self.id_actor) 
    
    class Meta:
        db_table='personajes'
        verbose_name='personaje'
        verbose_name_plural='personajes'
        ordering = ['nombre_personaje']


class aparecen(models.Model):
    id_aparicion = AutoField(primary_key=True)
    id_personaje= models.ForeignKey(personaje, on_delete=CASCADE, db_column='id_personaje')
    id_temporada = models.ForeignKey(temporada, on_delete=CASCADE, db_column='id_temporada')
    rol=models.CharField(max_length=10)
    
    class Meta:
        db_table='aparecen'
        verbose_name='aparece'
        verbose_name_plural='aparecen'
        ordering = ['id_aparicion']
