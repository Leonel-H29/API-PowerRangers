from rest_framework import  viewsets
from rest_framework.authentication import TokenAuthentication 
from django.contrib.auth.mixins import PermissionRequiredMixin
#from rest_framework.decorators import action
#from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from Actor.models import actor, aparecen, personaje
from Actor.serializers import ActorSerializer, AparecenEnSerializer, PersonajeSerializer
#from django.contrib.auth.models import User
from rest_framework import permissions 
from User.permissions import SuperuserPermission, ReadOnlyPermission

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class ActoresViewSet(viewsets.ModelViewSet):
    queryset = actor.objects.all()
    serializer_class = ActorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nombre_actor', 'nombre_artistico']
    name = 'actores'
    depth = 1
    authentication_classes = [TokenAuthentication]
    permission_classes = [SuperuserPermission | ReadOnlyPermission]
    
    @swagger_auto_schema(
        operation_summary="Obtener un actor por su id",
        operation_description="Retorna un actor con la información completa.",
        responses={200: ActorSerializer()})
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Obtener todos los actores",
        operation_description="Retorna una lista con todos los actores.",
        responses={200: ActorSerializer(many=True)})
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Crear un nuevo actor",
        operation_description="Crea un nuevo actor con la información proporcionada.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'nombre_actor': openapi.Schema(type=openapi.TYPE_STRING, description='Nombre real del actor'),
                'nombre_artistico': openapi.Schema(type=openapi.TYPE_STRING, description='Nombre artístico del actor'),
                'foto': openapi.Schema(type=openapi.TYPE_STRING, description='URL de la foto del actor'),
                'biografia': openapi.Schema(type=openapi.TYPE_STRING, description='URL de la biografia del actor'),
            }
        ),
        responses={
            201: ActorSerializer(),
            400: 'Error en los datos enviados',
            401: 'No autenticado',
            403: 'Permiso denegado'
        },
        security=[{'Token de acceso': []}]
        )     
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Actualizar un actor existente",
        operation_description="Actualiza la información de un actor existente.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'nombre_actor': openapi.Schema(type=openapi.TYPE_STRING, description='Nombre real del actor'),
                'nombre_artistico': openapi.Schema(type=openapi.TYPE_STRING, description='Nombre artístico del actor'),
                'edad': openapi.Schema(type=openapi.TYPE_INTEGER, description='Edad del actor'),
                'pais': openapi.Schema(type=openapi.TYPE_STRING, description='País del actor'),
            }
        ),
        responses={200: ActorSerializer()})
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        request_body=ActorSerializer,
        operation_summary="Actualiza parcialmente un actor",
        operation_description='Actualiza parcialmente un actor existente',
        responses={
            200: 'Actor actualizado exitosamente',
            400: 'Error en los datos enviados',
            401: 'No autenticado',
            403: 'Permiso denegado',
            404: 'No encontrado'
        },
        security=[{'Token de acceso': []}]
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary="Elimina un actor",
        operation_description='Elimina un actor existente',
        responses={
            204: 'Actor eliminado exitosamente',
            401: 'No autenticado',
            403: 'Permiso denegado',
            404: 'No encontrado'
        },
        security=[{'Token de acceso': []}]
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    


    
class AparecenViewSet(viewsets.ModelViewSet):
    queryset = aparecen.objects.all()
    serializer_class = AparecenEnSerializer
    name = 'aparecen'
    depth = 1
    authentication_classes = [TokenAuthentication]
    permission_classes = [SuperuserPermission | ReadOnlyPermission]    



class PersonajesViewSet(viewsets.ModelViewSet):
    queryset = personaje.objects.all()
    serializer_class = PersonajeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['actor', 'nombre_personaje']
    name = 'personajes'
    depth = 1
    authentication_classes = [TokenAuthentication]
    permission_classes = [SuperuserPermission | ReadOnlyPermission]