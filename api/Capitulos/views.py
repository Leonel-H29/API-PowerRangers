from rest_framework import  viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import PermissionRequiredMixin
#from rest_framework.decorators import action
#from rest_framework.response import Response

from Capitulos.models import capitulo
from Capitulos.serializers import CapitulosSerializer
#from django.contrib.auth.models import User


class CapitulosViewSet(viewsets.ModelViewSet):
    queryset = capitulo.objects.all()
    serializer_class = CapitulosSerializer