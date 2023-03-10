from rest_framework import serializers
from Capitulos.models import capitulo

class CapitulosSerializer(serializers.ModelSerializer):
    class Meta:
        model = capitulo
        fields = (
            'id_capitulo',
            'numero_cap',
            'nombre',
            'descripcion',
            'temporada', 
        )
        read_only_fields = ['id_capitulo', 'temporada']