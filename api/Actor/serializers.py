from rest_framework import serializers
from Actor.models import actor, personaje, aparecen
from Temporadas.models import temporada
from Temporadas.serializers import TemporadaSerializer
#from .serializers import PersonajeSerializer

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
    actor = ActorSerializer(read_only=True)
    class Meta:
        model = personaje
        fields = (
            'id_personaje',
            'nombre_personaje',
            #'descripcion',
            'foto',
            'actor',
        )
        read_only_fields = ['id_personaje']


class AparecenEnSerializer(serializers.ModelSerializer):
    personaje = PersonajeSerializer(read_only=True)
    temporada = TemporadaSerializer(read_only=True)
    
    class Meta:
        model = aparecen
        fields = ('id_aparicion', 'personaje', 'temporada', 'rol')
        read_only_fields = ['id_aparicion']
    