from rest_framework import  viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import PermissionRequiredMixin
#from rest_framework.decorators import action
#from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from Capitulos.models import capitulo
from Capitulos.serializers import CapitulosSerializer
#from django.contrib.auth.models import User

from rest_framework import permissions 
from User.permissions import SuperuserPermission, ReadOnlyPermission

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class CapitulosViewSet(viewsets.ModelViewSet):
    queryset = capitulo.objects.all()
    serializer_class = CapitulosSerializer
    filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['numero_cap', 'temporada']
    filterset_fields = ['numero_cap']
    permission_classes = [SuperuserPermission | ReadOnlyPermission]

    @swagger_auto_schema(
        operation_summary="Obtener un capitulo por su id",
        operation_description="Retorna un capitulo con la información completa.",
        responses={200: CapitulosSerializer()})
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Obtener todos los capitulos",
        operation_description="Retorna una lista con todos los capitulos.",
        responses={200: CapitulosSerializer(many=True)})
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Crear un nueva capitulo",
        operation_description="Crea un nueva capitulo con la información proporcionada.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'numero_cap' : openapi.Schema(type=openapi.TYPE_INTEGER, description='Numero del capitulo'),
                'nombre': openapi.Schema(type=openapi.TYPE_STRING, description='Nombre real del capitulo'),
                'descripcion': openapi.Schema(type=openapi.TYPE_STRING, description='Descripcion de la temporada'),
                #'temporada': openapi.Schema(type=openapi.TYPE_INTEGER, description='Temporada a la que pertenece el capitulo'),              
            }
        ),
        responses={
            201: CapitulosSerializer(),
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
                'numero_cap' : openapi.Schema(type=openapi.TYPE_INTEGER, description='Numero del capitulo'),
                'nombre': openapi.Schema(type=openapi.TYPE_STRING, description='Nombre real del capitulo'),
                'descripcion': openapi.Schema(type=openapi.TYPE_STRING, description='Descripcion de la temporada'),
                #'temporada': openapi.Schema(type=openapi.TYPE_INTEGER, description='Temporada a la que pertenece el capitulo'),              
            }
        ),
        responses={200: CapitulosSerializer()})
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        request_body=CapitulosSerializer,
        operation_summary="Actualiza parcialmente un capitulo",
        operation_description='Actualiza parcialmente un capitulo existente',
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
        operation_summary="Elimina un capitulo",
        operation_description='Elimina un capitulo existente',
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