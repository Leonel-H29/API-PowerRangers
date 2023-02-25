from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import PermissionRequiredMixin
#from rest_framework.decorators import action
#from rest_framework.response import Response

from Temporadas.models  import temporada
from Temporadas.serializers import TemporadaSerializer
#from django.contrib.auth.models import User

"""
class TemporadasViewSet(viewsets.ModelViewSet):
    queryset = temporada.objects.all()
    serializer_class = TemporadaSerializer
"""

class TemporadasViewSet(viewsets.ModelViewSet):
    queryset = temporada.objects.all()
    serializer_class = TemporadaSerializer
    name = 'temporadas'
    depth = 1