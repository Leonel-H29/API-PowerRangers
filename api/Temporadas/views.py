from rest_framework import viewsets, generics
from rest_framework.authentication import TokenAuthentication 
from django.contrib.auth.mixins import PermissionRequiredMixin
#from rest_framework.decorators import action
#from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from Temporadas.models  import temporada
from Temporadas.serializers import TemporadaSerializer
#from django.contrib.auth.models import User
from User.permissions import SuperuserPermission, ReadOnlyPermission


from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class TemporadasViewSet(viewsets.ModelViewSet):
    queryset = temporada.objects.all()
    serializer_class = TemporadaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['numero_temporada', 'nombre', 'anio_estreno']
    name = 'temporadas'
    depth = 1
    authentication_classes = [TokenAuthentication]
    permission_classes = [SuperuserPermission | ReadOnlyPermission]

    @swagger_auto_schema(
        operation_summary="Obtener un temporada por su id",
        operation_description="Retorna un temporada con la información completa.",
        responses={200: TemporadaSerializer()})
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Obtener todas las temporadaes",
        operation_description="Retorna una lista con todas las temporadaes.",
        responses={200: TemporadaSerializer(many=True)})
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Crear una nueva temporada",
        operation_description="Crea un nueva temporada con la información proporcionada.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'numero_temporada' : openapi.Schema(type=openapi.TYPE_INTEGER, description='Numero de temporada'),
                'nombre' : openapi.Schema(type=openapi.TYPE_STRING, description='Nombre de esa temporada'),
                'descripcion': openapi.Schema(type=openapi.TYPE_STRING, description='Descripcion de la temporada'),
                'foto' : openapi.Schema(type=openapi.TYPE_STRING, description='URL de la foto de la temporada'),
                'anio_estreno': openapi.Schema(type=openapi.TYPE_INTEGER, description='Año de estreno de la temporada'),
                'cancion' : openapi.Schema(type=openapi.TYPE_STRING, description='Nombre de la cancion de esa temporada'),
                'basada_en' : openapi.Schema(type=openapi.TYPE_STRING, description='Nombre del serie, novela, libro, etc en que se basa esa temporada'),
                'tematica' : openapi.Schema(type=openapi.TYPE_STRING, description='La tematica en que se basa esa temporada'),
            }
        ),
        responses={
            201: TemporadaSerializer(),
            400: 'Error en los datos enviados',
            401: 'No autenticado',
            403: 'Permiso denegado'
        },
        security=[{'Token de acceso': []}]
        )     
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Actualizar un temporada existente",
        operation_description="Actualiza la información de un temporada existente.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'numero_temporada' : openapi.Schema(type=openapi.TYPE_INTEGER, description='Numero de temporada'),
                'nombre' : openapi.Schema(type=openapi.TYPE_STRING, description='Nombre de esa temporada'),
                'descripcion': openapi.Schema(type=openapi.TYPE_STRING, description='Descripcion de la temporada'),
                'foto' : openapi.Schema(type=openapi.TYPE_STRING, description='URL de la foto de la temporada'),
                'anio_estreno': openapi.Schema(type=openapi.TYPE_INTEGER, description='Año de estreno de la temporada'),
                'cancion' : openapi.Schema(type=openapi.TYPE_STRING, description='Nombre de la cancion de esa temporada'),
                'basada_en' : openapi.Schema(type=openapi.TYPE_STRING, description='Nombre del serie, novela, libro, etc en que se basa esa temporada'),
                'tematica' : openapi.Schema(type=openapi.TYPE_STRING, description='La tematica en que se basa esa temporada'),
            }
        ),
        responses={200: TemporadaSerializer()})
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        request_body=TemporadaSerializer,
        operation_summary="Actualiza parcialmente una temporada",
        operation_description='Actualiza parcialmente una temporada existente',
        responses={
            200: 'Temporada actualizada exitosamente',
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
        operation_summary="Elimina una temporada",
        operation_description='Elimina una temporada existente',
        responses={
            204: 'Temporada eliminada exitosamente',
            401: 'No autenticado',
            403: 'Permiso denegado',
            404: 'No encontrado'
        },
        security=[{'Token de acceso': []}]
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)