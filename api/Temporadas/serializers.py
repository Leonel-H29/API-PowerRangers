from rest_framework import serializers
from Temporadas.models import temporada
#from Capitulos.models import capitulo
from Capitulos.serializers import CapitulosSerializer

class TemporadaSerializer(serializers.ModelSerializer):
    capitulos = CapitulosSerializer(many=True, read_only=True) 
    class Meta:
        model = temporada
        fields = (
            'id_temporada',
            'numero_temporada',
            'nombre',
            'descripcion',
            'anio_estreno',
            'foto',
            'cancion',
            'basada_en',
            'tematica',
            'capitulos',
            'updated'  
        )
        read_only_fields = ['id_temporada', 'capitulos']