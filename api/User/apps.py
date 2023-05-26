from django.apps import AppConfig
#from User.models import User
from api.settings.development import FILE_ENV as env 
#from api.settings.production import FILE_ENV as proenv

class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'User'
    
    def ready(self):
        from User.models import User
        # Llama a create_superuser_if_not_exists cuando la aplicación se carga
        if env:
            from api.settings.development import DJANGO_SUPERUSER_USERNAME, DJANGO_SUPERUSER_EMAIL, DJANGO_SUPERUSER_PASSWORD
            User.create_superuser_if_not_exists(DJANGO_SUPERUSER_USERNAME, DJANGO_SUPERUSER_EMAIL, DJANGO_SUPERUSER_PASSWORD)
        else:
            from api.settings.production import DJANGO_SUPERUSER_USERNAME, DJANGO_SUPERUSER_EMAIL, DJANGO_SUPERUSER_PASSWORD
            User.create_superuser_if_not_exists(DJANGO_SUPERUSER_USERNAME, DJANGO_SUPERUSER_EMAIL, DJANGO_SUPERUSER_PASSWORD)
