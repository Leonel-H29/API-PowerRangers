from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.db.models.fields import AutoField
from Temporadas.models import temporada

# Create your models here.
class actor(models.Model):
    id_actor= AutoField(primary_key=True, help_text='ID del actor')
    nombre_actor=models.CharField(max_length=80, help_text='Nombre real del actor')
    nombre_artistico=models.CharField(max_length=80, blank=True, null=True, help_text='Nombre artistico del actor')
    foto=models.CharField(max_length=300, help_text='URL de la foto del actor')
    biografia=models.CharField(max_length=300, help_text='URL de la biografia del actor')
    created = models.DateTimeField(auto_now_add=True, help_text='Fecha de creacion del registro')
    updated = models.DateTimeField(auto_now_add=True, help_text='Fecha de actualizacion del registro')
    
    def __str__(self):
        return str(self.id_actor)  + self.nombre_actor
    
    class Meta :
        db_table='actor'
        verbose_name='actor'
        verbose_name_plural='actores'
        ordering = ['nombre_actor']


class personaje(models.Model):
    id_personaje= AutoField(primary_key=True, help_text='ID del personaje')
    nombre_personaje=models.CharField(max_length=80, unique=True, help_text='Nombre real del personaje')
    #descripcion=models.TextField(blank=True, null=True)
    foto=models.CharField(max_length=300, help_text='URL de la foto del personaje')
    #id_actor= models.ForeignKey(actor, on_delete=DO_NOTHING, db_column='id_actor')
    actor= models.ForeignKey(actor, on_delete=DO_NOTHING, db_column='id_actor',related_name='personajes', help_text='Datos del actor que interpreta al personaje')
    temporadas=models.ManyToManyField(temporada,through='Aparecen', related_name='personajes')
    created = models.DateTimeField(auto_now_add=True, help_text='Fecha de creacion del registro')
    updated = models.DateTimeField(auto_now_add=True, help_text='Fecha de actualizacion del registro')
    
    def __str__(self):
        return str(self.id_personaje) + ")- " + self.nombre_personaje 
    
    class Meta:
        db_table='personajes'
        verbose_name='personaje'
        verbose_name_plural='personajes'
        ordering = ['nombre_personaje']
        unique_together = ('nombre_personaje', 'actor')


class aparecen(models.Model):
    id_aparicion = AutoField(primary_key=True)
    personaje= models.ForeignKey(personaje, on_delete=CASCADE, db_column='id_personaje')
    temporada = models.ForeignKey(temporada, on_delete=CASCADE, db_column='id_temporada')
    rol=models.CharField(max_length=30)
    descripcion=models.TextField(blank=True, null=True)
    class Meta:
        db_table='aparecen'
        verbose_name='aparece'
        verbose_name_plural='aparecen'
        ordering = ['id_aparicion']
        unique_together = ('personaje', 'temporada')
