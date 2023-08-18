from rest_framework import viewsets, generics
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.mixins import PermissionRequiredMixin
# from rest_framework.decorators import action
# from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from Temporadas.models import temporada
from Temporadas.serializers import TemporadaSerializer
# from django.contrib.auth.models import User
from User.permissions import SuperuserPermission, ReadOnlyPermission


from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class TemporadasViewSet(viewsets.ModelViewSet):
    """
### Temporadas

#### Descripción:

Esta vista proporciona información sobre todas las temporadas de `Power Rangers` disponibles. 
Cada temporada representa un conjunto de episodios que conforman una historia específica dentro de la 
franquicia `Power Rangers`. 

#### Datos:

    | COLUMNA          | TIPO              | DESCRIPCION                                      |
    |------------------|-------------------|--------------------------------------------------|
    | id_temporada     | integer           | ID unico de la temporada                         |
    | numero_temporada | integer           | Numero de temporada                              |
    | nombre           | string            | Titulo asignado a la temporada                   |
    | descripcion      | string            | Descripcion de lo que sucede en la temporada     |
    | anio_estreno     | integer           | Año de estreno de la temporada                   |
    | foto             | string            | URL relacionada a la temporada                   |
    | cancion          | string            | Cancion oficial de la temporada                  |
    | basada_en        | string            | Serie, Libro, etc en la que se basa la temporada |
    | tematica         | string            | Tematica que abarca la temporada                 |
    | capitulos        | list (capitulo)   | Lista de los capitulos emitidos en la temporada  |
    | updated          | string (datetime) | Fecha de actualizacion del registro              |       

    """
    queryset = temporada.objects.all()
    serializer_class = TemporadaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['numero_temporada', 'nombre', 'anio_estreno']
    name = 'temporadas'
    depth = 1
    authentication_classes = [TokenAuthentication]
    permission_classes = [SuperuserPermission | ReadOnlyPermission]

    # Documentacion en Swagger

    @swagger_auto_schema(
        operation_summary="Obtener un temporada por su id",
        operation_description="Retorna un temporada con la información completa.",
        responses={
            200: TemporadaSerializer(),
            400: 'No se ha encontrado la temporada solicitada',
            500: 'Se ha producido un error interno en el servidor'
        })
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Obtener todas las temporadaes",
        operation_description="Retorna una lista con todas las temporadaes.",
        responses={
            200: TemporadaSerializer(many=True),
            400: 'No se ha encontrado el listado',
            500: 'Se ha producido un error interno en el servidor'
        })
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Crear una nueva temporada",
        operation_description="Crea un nueva temporada con la información proporcionada.",
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                required=True,
                type=openapi.TYPE_STRING,
                description='Token de acceso (Token access_token)'
            ),
        ],
        request_body=TemporadaSerializer,
        responses={
            201: 'Temporada creada exitosamente',
            400: 'Error en los datos enviados',
            401: 'No autenticado',
            403: 'Permiso denegado',
            500: 'Se ha producido un error interno en el servidor'
        },
        # security=[{'Token de acceso': []}]
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Actualizar un temporada existente",
        operation_description="Actualiza la información de un temporada existente.",
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                required=True,
                type=openapi.TYPE_STRING,
                description='Token de acceso (Token access_token)'
            ),
        ],
        request_body=TemporadaSerializer,
        responses={
            200: 'Temporada actualizada exitosamente',
            400: 'Error en los datos enviados',
            401: 'No autenticado',
            403: 'Permiso denegado',
            404: 'No encontrado',
            500: 'Se ha producido un error interno en el servidor'
        })
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=TemporadaSerializer,
        operation_summary="Actualiza parcialmente una temporada",
        operation_description='Actualiza parcialmente una temporada existente',
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                required=True,
                type=openapi.TYPE_STRING,
                description='Token de acceso (Token access_token)'
            ),
        ],
        responses={
            200: 'Temporada actualizada exitosamente',
            400: 'Error en los datos enviados',
            401: 'No autenticado',
            403: 'Permiso denegado',
            404: 'No encontrado',
            500: 'Se ha producido un error interno en el servidor'
        },
        # security=[{'Token de acceso': []}]
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Elimina una temporada",
        operation_description='Elimina una temporada existente',
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                required=True,
                type=openapi.TYPE_STRING,
                description='Token de acceso (Token access_token)'
            ),
        ],
        responses={
            204: 'Temporada eliminada exitosamente',
            401: 'No autenticado',
            403: 'Permiso denegado',
            404: 'No encontrado',
            500: 'Se ha producido un error interno en el servidor'
        },
        # security=[{'Token de acceso': []}]
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
