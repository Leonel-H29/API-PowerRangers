from django.apps import AppConfig


class UserConfig(AppConfig):
    """
    Clase para el panel de `admin` de Django para el usuario
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'User'

    def ready(username='', email='', passw=''):
        """
        Funcion definida para establecer los pasos a seguir luego de que
        el panel de `admin` de Django este listo

        ### Args:
            - `username (str)`: Nombre de usuario para el admin
            - `email (str)`: Correo de usuario
            - `password (str)`: Contraseña del usuario
        """
        from User.models import User

        # Llama a create_superuser_if_not_exists cuando la aplicación se carga
        User.create_superuser_if_not_exists(username, email, passw)
