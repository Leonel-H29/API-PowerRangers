from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.db.models.fields import AutoField
from Temporadas.models import temporada

# Create your models here.


class capitulo(models.Model):
    """
    Modelo para todos los capitulos que se emitieron en una temporada especifica
    """
    id_capitulo = AutoField(
        primary_key=True, help_text='ID unico del capitulo'
    )
    numero_cap = models.PositiveIntegerField(help_text='Numero del capitulo')
    titulo = models.CharField(max_length=50, help_text='Titulo del capitulo')
    descripcion = models.TextField(
        blank=True, null=True, help_text='Descripcion de lo que sucede en el capitulo'
    )
    temporada = models.ForeignKey(
        temporada, on_delete=DO_NOTHING, db_column='id_temporada',
        related_name='capitulos', help_text='ID de la temporada a la que pertenece el capitulo'
    )
    created = models.DateTimeField(
        auto_now_add=True, help_text='Fecha de creacion del registro'
    )
    updated = models.DateTimeField(
        auto_now_add=True, help_text='Fecha de actualizacion del registro'
    )

    def __str__(self):
        return str(self.id_capitulo) + ")- " + self.titulo

    class Meta:
        db_table = 'capitulos'
        verbose_name = 'capitulo'
        verbose_name_plural = 'capitulos'
        ordering = ['temporada', 'numero_cap']
        unique_together = ('numero_cap', 'temporada')
