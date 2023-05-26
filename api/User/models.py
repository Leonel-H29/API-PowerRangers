from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']
    
    def create_superuser_if_not_exists(username, email, password):
        User = get_user_model()
        # Verificar si ya existe un superusuario con el mismo nombre o correo
        if not User.objects.filter(is_superuser=True).filter(models.Q(username=username) | models.Q(email=email)).exists():
            user=User.objects.create_superuser(username=username, email=email, password=password)
            user.save()
            print('Superusuario creado ...')
        else:
            print('El superusuario ya existe')

            