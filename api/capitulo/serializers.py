from rest_framework import serializers
from capitulo.models import capitulo

class CapitulosSerializer(serializers.ModelSerializer):
    class Meta:
        model = capitulo
        fields = (
            'id_capitulo',
            'nombre',
            'descripcion',
            'id_temporada', 
        )
        read_only_fields = ['id_capitulo']