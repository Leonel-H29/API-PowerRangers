from rest_framework import  viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import PermissionRequiredMixin
#from rest_framework.decorators import action
#from rest_framework.response import Response

from temporada.models  import temporada
from temporada.serializers import TemporadaSerializer
#from django.contrib.auth.models import User


class TemporadasViewSet(viewsets.ModelViewSet):
    queryset = temporada.objects.all()
    serializer_class = TemporadaSerializer