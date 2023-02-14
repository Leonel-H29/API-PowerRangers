from rest_framework import serializers
from actor.models import actor, personaje

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = actor
        fields = (
            'id_actor',
            'nombre_actor',
            'nombre_artistico',
            'foto',
            'biografia'
        )
        read_only_fields = ['id_actor']
        

class PersonajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = personaje
        fields = (
            'id_personaje',
            'nombre_personaje',
            'descripcion',
            'foto',
        )
        read_only_fields = ['id_personaje']