from django.apps import AppConfig

class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'User'
    
    def ready(username='', email='', passw=''):
        from User.models import User
 
        # Llama a create_superuser_if_not_exists cuando la aplicación se carga
        User.create_superuser_if_not_exists(username, email, passw)
