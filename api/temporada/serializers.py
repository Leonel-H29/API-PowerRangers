from rest_framework import serializers
from temporada.models import temporada

class TemporadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = temporada
        fields = (
            'id_temporada'
            'nombre',
            'descripcion',
            'anio_estreno',
            'foto',
            'cancion',
            'basada_en'
        )
        read_only_fields = ['id_temporada']