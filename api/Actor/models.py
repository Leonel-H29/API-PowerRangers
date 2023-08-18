from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.db.models.fields import AutoField
from Temporadas.models import temporada

# Create your models here.


class actor(models.Model):
    """
    Modelo para los actores que participaron en la serie 
    """
    id_actor = AutoField(primary_key=True, help_text='ID unico del actor')
    nombre_actor = models.CharField(
        max_length=80, help_text='Nombre real del actor'
    )
    nombre_artistico = models.CharField(
        max_length=80, help_text='Nombre artistico del actor'
    )
    foto = models.CharField(
        max_length=300, help_text='URL de la foto del actor'
    )
    biografia = models.CharField(
        max_length=300, help_text='URL de la biografia del actor'
    )
    created = models.DateTimeField(
        auto_now_add=True, help_text='Fecha de creacion del registro'
    )
    updated = models.DateTimeField(
        auto_now_add=True, help_text='Fecha de actualizacion del registro'
    )

    def __str__(self):
        return str(self.id_actor) + self.nombre_actor

    class Meta:
        db_table = 'actor'
        verbose_name = 'actor'
        verbose_name_plural = 'actores'
        ordering = ['nombre_actor']
        unique_together = ('nombre_actor', 'nombre_artistico')


class personaje(models.Model):
    """
    Modelo para los personajes que aparecen en la serie
    """
    id_personaje = AutoField(
        primary_key=True, help_text='ID unico del personaje'
    )
    nombre_personaje = models.CharField(
        max_length=80, help_text='Nombre real del personaje'
    )
    # descripcion=models.TextField(blank=True, null=True)
    foto = models.CharField(
        max_length=300, help_text='URL de la foto del personaje'
    )
    actor = models.ForeignKey(
        actor, on_delete=DO_NOTHING, db_column='id_actor',
        related_name='personajes', help_text='Id del actor que interpreta al personaje'
    )
    temporadas = models.ManyToManyField(
        temporada, through='Aparecen', related_name='personajes'
    )
    created = models.DateTimeField(
        auto_now_add=True, help_text='Fecha de creacion del registro'
    )
    updated = models.DateTimeField(
        auto_now_add=True, help_text='Fecha de actualizacion del registro'
    )

    def __str__(self):
        return str(self.id_personaje) + ")- " + self.nombre_personaje

    class Meta:
        db_table = 'personajes'
        verbose_name = 'personaje'
        verbose_name_plural = 'personajes'
        ordering = ['nombre_personaje']
        unique_together = ('nombre_personaje', 'actor')


class aparecen(models.Model):
    """
    Modelo que representa la relacion de N:N entre `temporada` y `personaje`.
    Es decir, en una temporada hay muchos personajes y un personaje 
    puede aparecer en varias temporadas 
    """
    id_aparicion = AutoField(
        primary_key=True, help_text='ID unico de la aparicion del personaje en la temporada'
    )
    personaje = models.ForeignKey(
        personaje, on_delete=CASCADE, db_column='id_personaje', help_text='Datos del personaje'
    )
    temporada = models.ForeignKey(
        temporada, on_delete=CASCADE, db_column='id_temporada', help_text='Datos de la temporada'
    )
    rol = models.CharField(
        max_length=30, help_text='El rol que ocupa el personaje en la temporada'
    )
    descripcion = models.TextField(
        blank=True, null=True, help_text='Descripcion del rol del personaje en esta temporada'
    )

    class Meta:
        db_table = 'aparecen'
        verbose_name = 'aparece'
        verbose_name_plural = 'aparecen'
        ordering = ['id_aparicion']
        unique_together = ('personaje', 'temporada')
