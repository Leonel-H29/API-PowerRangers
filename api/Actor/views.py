from rest_framework import  viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import PermissionRequiredMixin
#from rest_framework.decorators import action
#from rest_framework.response import Response

from Actor.models import actor, aparecen, personaje
from Actor.serializers import ActorSerializer, AparecenEnSerializer, PersonajeSerializer
#from django.contrib.auth.models import User


class ActoresViewSet(viewsets.ModelViewSet):
    queryset = actor.objects.all()
    serializer_class = ActorSerializer
    name = 'actores'
    depth = 1
    
    
class AparecenViewSet(viewsets.ModelViewSet):
    queryset = aparecen.objects.all()
    serializer_class = AparecenEnSerializer
    name = 'aparecen'
    depth = 1
    
class PersonajesViewSet(viewsets.ModelViewSet):
    queryset = personaje.objects.all()
    serializer_class = PersonajeSerializer
    name = 'personajes'
    depth = 1