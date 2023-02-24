from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.db.models.fields import AutoField
from Temporadas.models import temporada

# Create your models here.
class capitulo(models.Model):
    id_capitulo = AutoField(primary_key=True)
    nombre=models.CharField(max_length=20)
    descripcion=models.TextField(blank=True, null=True)
    id_temporada = models.ForeignKey(temporada, on_delete=DO_NOTHING, db_column='id_temporada')
    
    def __str__(self):
        return str(self.id_capitulo) + ")- " + self.nombre

    class Meta:
        db_table='capitulos'
        verbose_name='capitulo'
        verbose_name_plural='capitulos'
        ordering = ['id_capitulo']
