from rest_framework import  viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import PermissionRequiredMixin
#from rest_framework.decorators import action
#from rest_framework.response import Response

from actor.models import actor
from actor.serializers import ActorSerializer
#from django.contrib.auth.models import User


class ActoresViewSet(viewsets.ModelViewSet):
    queryset = actor.objects.all()
    serializer_class = ActorSerializer