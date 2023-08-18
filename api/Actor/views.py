from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.mixins import PermissionRequiredMixin
# from rest_framework.decorators import action
# from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from Actor.models import actor, aparecen, personaje
from Actor.serializers import ActorSerializer, AparecenEnSerializer, PersonajeSerializer
# from django.contrib.auth.models import User
from rest_framework import permissions
from User.permissions import SuperuserPermission, ReadOnlyPermission

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class ActoresViewSet(viewsets.ModelViewSet):
    """
### Actores

#### Descripción: 

Esta vista contiene información sobre los actores que han interpretado roles 
en las diferentes temporadas de `Power Rangers`. Los actores son quienes dan vida a los personajes 
icónicos de la serie.


#### Datos:

    | COLUMNA          | TIPO               | DESCRIPCION                                                 |
    |------------------|--------------------|-------------------------------------------------------------|
    | id_actor	       | integer            | ID unico del actor                                          |
    | nombre_actor	   | string             | Nombre real del actor                                       |
    | nombre_artistico | string             | Nombre artistico del actor                                  |
    | foto	           | string             | URL de la foto del actor                                    |
    | biografia        | string             | URL de la biografia del actor                               |
    | personajes	   | list (personaje)   | Lista de los personajes que interpreta el actor en la serie |
    | updated          | string (datetime)  | Fecha de actualizacion del registro                         | 

    """
    queryset = actor.objects.all()
    serializer_class = ActorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nombre_actor', 'nombre_artistico']
    name = 'actores'
    depth = 1
    authentication_classes = [TokenAuthentication]
    permission_classes = [SuperuserPermission | ReadOnlyPermission]

    # Documentacion en Swagger

    @swagger_auto_schema(
        operation_summary="Obtener un actor por su id",
        operation_description="Retorna un actor con la información completa.",
        responses={
            200: ActorSerializer(),
            400: 'No se ha encontrado el actor solicitado',
            500: 'Se ha producido un error interno en el servidor'
        })
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Obtener todos los actores",
        operation_description="Retorna una lista con todos los actores.",
        responses={
            200: ActorSerializer(many=True),
            400: 'No se ha encontrado el listado',
            500: 'Se ha producido un error interno en el servidor'
        })
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Crear un nuevo actor",
        operation_description="Crea un nuevo actor con la información proporcionada.",
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                required=True,
                type=openapi.TYPE_STRING,
                description='Token de acceso (Token access_token)'
            ),
        ],
        request_body=ActorSerializer,
        responses={
            201: 'Actor creado exitosamente',
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
        operation_summary="Actualizar un actor existente",
        operation_description="Actualiza la información de un actor existente.",
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                required=True,
                type=openapi.TYPE_STRING,
                description='Token de acceso (Token access_token)'
            ),
        ],
        request_body=ActorSerializer,
        responses={
            200: 'Actor actualizado exitosamente',
            400: 'Error en los datos enviados',
            401: 'No autenticado',
            403: 'Permiso denegado',
            404: 'No encontrado',
            500: 'Se ha producido un error interno en el servidor'
        })
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=ActorSerializer,
        operation_summary="Actualiza parcialmente un actor",
        operation_description='Actualiza parcialmente un actor existente',
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
            200: 'Actor actualizado exitosamente',
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
        operation_summary="Elimina un actor",
        operation_description='Elimina un actor existente',
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
            204: 'Actor eliminado exitosamente',
            401: 'No autenticado',
            403: 'Permiso denegado',
            404: 'No encontrado',
            500: 'Se ha producido un error interno en el servidor'
        },
        # security=[{'Token de acceso': []}]
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class AparecenViewSet(viewsets.ModelViewSet):
    """
### Aparecen

#### Descripción: 

Esta vista muestra la relación entre los personajes y las temporadas en las que aparecen en la serie `Power Rangers`. 
Es una relación N:N que vincula los personajes específicos con las temporadas en las que han participado. 

#### Datos:

    | COLUMNA          | TIPO              | DESCRIPCION                                            |
    |------------------|-------------------|--------------------------------------------------------|
    | id_aparicion	   | integer           | ID unico de la aparicion del personaje en la temporada | 
    | personaje	       | dict(personaje)   | Objeto personaje                                       |
    | temporada	       | dict (temporada)  | Objeto temporada                                       |
    | rol              | string            | El rol que ocupa el personaje en la temporada          |
    | descripcion      | string            | Descripcion del rol del personaje en esta temporada    |

    """
    queryset = aparecen.objects.all()
    serializer_class = AparecenEnSerializer
    name = 'aparecen'
    depth = 1
    authentication_classes = [TokenAuthentication]
    permission_classes = [SuperuserPermission | ReadOnlyPermission]

    # Documentacion en Swagger

    @swagger_auto_schema(
        operation_summary="Obtener una aparicion por su id",
        operation_description="Retorna una aparicion con la información completa.",
        responses={
            200: AparecenEnSerializer(),
            400: 'No se ha encontrado la aparicion solicitada',
            500: 'Se ha producido un error interno en el servidor'
        })
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Obtener todas las apariciones",
        operation_description="Retorna una lista con todas las apariciones.",
        responses={
            200: AparecenEnSerializer(many=True),
            400: 'No se ha encontrado el listado',
            500: 'Se ha producido un error interno en el servidor'
        })
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Crear una nueva aparicion",
        operation_description="Crea una nueva aparicion con la información proporcionada.",
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                required=True,
                type=openapi.TYPE_STRING,
                description='Token de acceso (Token access_token)'
            ),
        ],
        request_body=AparecenEnSerializer,
        responses={
            201: 'Aparicion creada exitosamente',
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
        operation_summary="Actualizar una aparicion existente",
        operation_description="Actualiza la información de una aparicion existente.",
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                required=True,
                type=openapi.TYPE_STRING,
                description='Token de acceso (Token access_token)'
            ),
        ],
        request_body=AparecenEnSerializer,
        responses={
            200: 'Aparicion actualizada exitosamente',
            400: 'Error en los datos enviados',
            401: 'No autenticado',
            403: 'Permiso denegado',
            404: 'No encontrado',
            500: 'Se ha producido un error interno en el servidor'
        })
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=AparecenEnSerializer,
        operation_summary="Actualiza parcialmente una aparicion",
        operation_description='Actualiza parcialmente una aparicion existente',
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
            200: 'Aparicion actualizada exitosamente',
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
        operation_summary="Elimina una aparicion",
        operation_description='Elimina una aparicion existente',
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
            204: 'Aparicion eliminada exitosamente',
            401: 'No autenticado',
            403: 'Permiso denegado',
            404: 'No encontrado',
            500: 'Se ha producido un error interno en el servidor'
        },
        # security=[{'Token de acceso': []}]
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class PersonajesViewSet(viewsets.ModelViewSet):
    """
### Personajes

#### Descripción: 

En esta vista, encontrarás información sobre los personajes icónicos de `Power Rangers`. Cada personaje representa 
un héroe, villano u otro individuo importante que forma parte de la historia de la serie. 

#### Datos:

    | COLUMNA           | TIPO              | DESCRIPCION                              |
    |-------------------|-------------------|------------------------------------------|
    | id_personaje	    | integer           | ID unico del personaje                   |
    | nombre_personaje	| string            | Nombre real del personaje                |
    | foto	            | string            | URL de la foto del personaje             | 
    | actor	            | integer           | Id del actor que interpreta al personaje |
    | updated           | string (datetime) | Fecha de actualizacion del registro      | 

    """
    queryset = personaje.objects.all()
    serializer_class = PersonajeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['actor', 'nombre_personaje']
    name = 'personajes'
    depth = 1
    authentication_classes = [TokenAuthentication]
    permission_classes = [SuperuserPermission | ReadOnlyPermission]

    # Documentacion en Swagger

    @swagger_auto_schema(
        operation_summary="Obtener un personaje por su id",
        operation_description="Retorna un personaje con la información completa.",
        responses={
            200: PersonajeSerializer(),
            400: 'No se ha encontrado el personaje solicitado',
            500: 'Se ha producido un error interno en el servidor'
        })
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Obtener todos los personajes",
        operation_description="Retorna una lista con todos los personajes.",
        responses={
            200: PersonajeSerializer(many=True),
            400: 'No se ha encontrado el listado',
            500: 'Se ha producido un error interno en el servidor'
        })
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Crear un nuevo personaje",
        operation_description="Crea un nuevo personaje con la información proporcionada.",
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                required=True,
                type=openapi.TYPE_STRING,
                description='Token de acceso (Token access_token)'
            ),
        ],
        request_body=PersonajeSerializer,
        responses={
            201: 'Personaje creado exitosamente',
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
        operation_summary="Actualizar un personaje existente",
        operation_description="Actualiza la información de un personaje existente.",
        manual_parameters=[
            openapi.Parameter(
                name='Authorization',
                in_=openapi.IN_HEADER,
                required=True,
                type=openapi.TYPE_STRING,
                description='Token de acceso (Token access_token)'
            ),
        ],
        request_body=PersonajeSerializer,
        responses={
            200: 'Personaje actualizado exitosamente',
            400: 'Error en los datos enviados',
            401: 'No autenticado',
            403: 'Permiso denegado',
            404: 'No encontrado',
            500: 'Se ha producido un error interno en el servidor'
        })
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=PersonajeSerializer,
        operation_summary="Actualiza parcialmente un personaje",
        operation_description='Actualiza parcialmente un personaje existente',
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
            200: 'Personaje actualizado exitosamente',
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
        operation_summary="Elimina un personaje",
        operation_description='Elimina un personaje existente',
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
            204: 'Personaje eliminado exitosamente',
            401: 'No autenticado',
            403: 'Permiso denegado',
            404: 'No encontrado',
            500: 'Se ha producido un error interno en el servidor'
        },
        # security=[{'Token de acceso': []}]
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
