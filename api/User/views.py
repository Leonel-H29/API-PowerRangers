"""Users views."""

# Django REST Framework
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Serializers
from User.serializers import UserLoginSerializer, UserModelSerializer

# Models
from User.models import User

#API SWAGGER
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class UserViewSet(viewsets.GenericViewSet):

    queryset = User.objects.filter(is_active=True)
    serializer_class = UserModelSerializer
    lookup_field = 'username'

    @swagger_auto_schema(
        operation_summary="Inicio de sesion de un usuario",
        operation_description="Permite a un usuario iniciar sesión en el sistema mediante su correo electrónico y contraseña.",
        
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Correo del usuario'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Contraseña del usuario'), 
            }
        ),
        responses={
            #200: 'Inicio de sesion exitoso',
            201: 'Inicio de sesion exitoso',
            400: 'Usuario o contraseña no validos',
            500: 'Se ha producido un error interno en el servidor'
    })
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
        
        #return Response({'message': 'Inicio de sesion'}, status=status.HTTP_200_OK)
    
        
        

    """
    manual_parameters=[
            openapi.Parameter(
                name='Email',
                in_=openapi.IN_QUERY,
                required=True,
                type=openapi.TYPE_STRING,
                description='Ingrese su correo electronico'
            ),
            openapi.Parameter(
                name='Password',
                in_=openapi.IN_QUERY,
                required=True,
                type=openapi.TYPE_STRING,
                description='Ingrese su contraseña'
            ),
        ],
    @action(detail=False, methods=['post'])
    def signup(self, request):
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)
    """
    
    