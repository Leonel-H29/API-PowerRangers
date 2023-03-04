from rest_framework import viewsets, generics
from rest_framework import permissions 
from django.contrib.auth.mixins import PermissionRequiredMixin
#from rest_framework.decorators import action
#from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from Temporadas.models  import temporada
from Temporadas.serializers import TemporadaSerializer
#from django.contrib.auth.models import User

"""
class TemporadasViewSet(viewsets.ModelViewSet):
    queryset = temporada.objects.all()
    serializer_class = TemporadaSerializer
"""


class TemporadasPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        elif request.method == 'GET':
            return True
        else:
            return False

class TemporadasViewSet(viewsets.ModelViewSet):
    queryset = temporada.objects.all()
    serializer_class = TemporadaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['numero_temporada', 'nombre', 'anio_estreno']
    name = 'temporadas'
    depth = 1
    permission_classes = [TemporadasPermission]