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



class CapitulosViewSet(viewsets.ModelViewSet):
    queryset = capitulo.objects.all()
    serializer_class = CapitulosSerializer
    filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['numero_cap', 'temporada']
    filterset_fields = ['numero_cap']
    permission_classes = [SuperuserPermission | ReadOnlyPermission]