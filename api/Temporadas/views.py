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


class TemporadasViewSet(viewsets.ModelViewSet):
    queryset = temporada.objects.all()
    serializer_class = TemporadaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['numero_temporada', 'nombre', 'anio_estreno']
    name = 'temporadas'
    depth = 1
    authentication_classes = [TokenAuthentication]
    permission_classes = [SuperuserPermission | ReadOnlyPermission]