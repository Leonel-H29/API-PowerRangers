"""Users views."""

# Django REST Framework
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Serializers
from User.serializers import UserLoginSerializer, UserModelSerializer

# Models
from User.models import User

class UserViewSet(viewsets.GenericViewSet):

    queryset = User.objects.filter(is_active=True)
    serializer_class = UserModelSerializer
    lookup_field = 'username'


    @action(detail=False, methods=['post'])
    def login(self, request):
        """User sign in."""
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user, token = serializer.save()
            data = {
                'user': UserModelSerializer(user).data,
                'access_token': token,
                'message': 'Inicio de sesion exitoso',
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Usuario o contraseña no validos'}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({'message': 'Inicio de sesion'}, status=status.HTTP_200_OK)

    """
    @action(detail=False, methods=['post'])
    def signup(self, request):
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)
    """