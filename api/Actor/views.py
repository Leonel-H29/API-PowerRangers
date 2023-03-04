from rest_framework import  viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import PermissionRequiredMixin
#from rest_framework.decorators import action
#from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from Actor.models import actor, aparecen, personaje
from Actor.serializers import ActorSerializer, AparecenEnSerializer, PersonajeSerializer
#from django.contrib.auth.models import User
from rest_framework import permissions 


class ActoresPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        elif request.method == 'GET':
            return True
        else:
            return False



class ActoresViewSet(viewsets.ModelViewSet):
    queryset = actor.objects.all()
    serializer_class = ActorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nombre_actor', 'nombre_artistico']
    name = 'actores'
    depth = 1
    permission_classes = [ActoresPermission]
    
    
class AparecenViewSet(viewsets.ModelViewSet):
    queryset = aparecen.objects.all()
    serializer_class = AparecenEnSerializer
    name = 'aparecen'
    depth = 1
    permission_classes = [ActoresPermission]
    
class PersonajesViewSet(viewsets.ModelViewSet):
    queryset = personaje.objects.all()
    serializer_class = PersonajeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['actor', 'nombre_personaje']
    name = 'personajes'
    depth = 1
    permission_classes = [ActoresPermission]