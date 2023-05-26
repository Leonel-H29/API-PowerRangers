from django.apps import AppConfig
import sys
import time

class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'User'
    
    def ready(self):
        from User.models import User
        #Verifico si estoy desarrollando en el entorno de desarrollo o produccion
        if '--settings=api.settings.development' in sys.argv:
            from api.settings.development import DJANGO_SUPERUSER_USERNAME, DJANGO_SUPERUSER_EMAIL, DJANGO_SUPERUSER_PASSWORD
            username=DJANGO_SUPERUSER_USERNAME 
            email=DJANGO_SUPERUSER_EMAIL 
            passw=DJANGO_SUPERUSER_PASSWORD
            print('Controlando el superusuario en entorno de desarrollo')
            time.sleep(2)
        else:
            from api.settings.production import DJANGO_SUPERUSER_USERNAME, DJANGO_SUPERUSER_EMAIL, DJANGO_SUPERUSER_PASSWORD
            username=DJANGO_SUPERUSER_USERNAME 
            email=DJANGO_SUPERUSER_EMAIL 
            passw=DJANGO_SUPERUSER_PASSWORD
            print('Controlando el superusuario en entorno de produccion')
            time.sleep(2)
            
        # Llama a create_superuser_if_not_exists cuando la aplicación se carga
        User.create_superuser_if_not_exists(username, email, passw)
