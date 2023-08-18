from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import AutoField

# Create your models here.


class temporada(models.Model):
    """
    Modelo para todas las temporadas de las serie 
    """
    id_temporada = AutoField(
        primary_key=True, help_text='ID unico de la temporada'
    )
    numero_temporada = models.PositiveIntegerField(
        unique=True, help_text='Numero de temporada'
    )
    nombre = models.CharField(
        max_length=50, help_text='Titulo asignado a la temporada'
    )
    descripcion = models.TextField(
        blank=True, null=True,
        help_text='Descripcion de lo que sucede en la temporada'
    )
    foto = models.CharField(
        max_length=260, help_text='URL relacionada a la temporada'
    )
    anio_estreno = models.PositiveIntegerField(
        help_text='Año de estreno de la temporada'
    )
    cancion = models.CharField(
        max_length=260, help_text='Cancion oficial de la temporada'
    )
    basada_en = models.CharField(
        max_length=50,
        help_text='Serie, Libro, etc en la que se basa la temporada'
    )
    tematica = models.CharField(
        max_length=100, help_text='Tematica que abarca la temporada'
    )
    created = models.DateTimeField(
        auto_now_add=True, help_text='Fecha de creacion del registro'
    )
    updated = models.DateTimeField(
        auto_now_add=True, help_text='Fecha de actualizacion del registro'
    )

    def __str__(self):
        return str(self.id_temporada) + ")- " + str(self.numero_temporada) + "-- " + self.nombre

    class Meta:
        db_table = 'temporadas'
        verbose_name = 'temporada'
        verbose_name_plural = 'temporadas'
        ordering = ['numero_temporada']
        unique_together = ('numero_temporada', 'nombre')
