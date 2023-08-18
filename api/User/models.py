from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
import time
from colorama import Fore
# Create your models here.


class User(AbstractUser):
    """
    Modelo personalizado para el usuario en esta aplicación
    """
    email = models.EmailField(max_length=254, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    def create_superuser_if_not_exists(username, email, password):
        """
        La función se encarga de controlar que en caso de que el superusuario no exista en la 
        base de datos, pueda crear automaticamente dicho usuario cuando se levante la aplicación.


        ### Args:
            - `username (str)`: Nombre de usuario para el admin
            - `email (str)`: Correo de usuario
            - `password (str)`: Contraseña del usuario
        """
        User = get_user_model()
        if username != '' and email != '' and password != '':
            # Verificar si ya existe un superusuario con el mismo nombre o correo
            if not User.objects.filter(is_superuser=True).filter(models.Q(username=username) | models.Q(email=email)).exists():
                user = User.objects.create_superuser(
                    username=username, email=email, password=password)
                user.save()
                print(Fore.GREEN + 'Superusuario creado ...')
                time.sleep(2)
            else:
                print(Fore.RESET + 'El superusuario ya existe!')
                time.sleep(2)
