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
    tematica=models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id_temporada) + ")- " + str(self.numero_temporada)+ "-- " +self.nombre
    
    class Meta:
        db_table='temporadas'
        verbose_name='temporada'
        verbose_name_plural='temporadas'
        ordering = ['numero_temporada']
        unique_together = ('numero_temporada', 'nombre')