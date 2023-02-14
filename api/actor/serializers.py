from rest_framework import serializers
from actor.models import actor, personaje, aparecen

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
        
        
class AparecenEnSerializer(serializers.ModelSerializer):
    class Meta:
        model = aparecen
        fields = (
            'id_aparicion', 
            'id_personaje',
            'id_temporada', 
            'rol'
        )
        read_only_fields = ['id_aparicion', 'id_personaje', 'id_temporada']