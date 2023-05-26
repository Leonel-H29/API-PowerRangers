from time import sleep
import sys
from django.core.management.base import BaseCommand
from User.apps import UserConfig 


class Command(BaseCommand):
    help = 'Wait for create superuser'

    def handle(self, *args, **options):
        comand_python='create_admin'
        #sys.argv.append(comand_python)
        #print(sys.argv)
        
        try:
            #Verifico si estoy desarrollando en el entorno de desarrollo o produccion
            if comand_python in sys.argv and '--settings=api.settings.development' in sys.argv:
                from api.settings.development import DJANGO_SUPERUSER_USERNAME, DJANGO_SUPERUSER_EMAIL, DJANGO_SUPERUSER_PASSWORD
                username=DJANGO_SUPERUSER_USERNAME 
                email=DJANGO_SUPERUSER_EMAIL 
                passw=DJANGO_SUPERUSER_PASSWORD
                self.stdout.write('Controlando el superusuario en entorno de desarrollo ...')
                sleep(2)
            elif comand_python in sys.argv and '--settings=api.settings.production':
                from api.settings.production import DJANGO_SUPERUSER_USERNAME, DJANGO_SUPERUSER_EMAIL, DJANGO_SUPERUSER_PASSWORD
                username=DJANGO_SUPERUSER_USERNAME 
                email=DJANGO_SUPERUSER_EMAIL 
                passw=DJANGO_SUPERUSER_PASSWORD
                self.stdout.write('Controlando el superusuario en entorno de produccion ...')
                sleep(2)
                
            UserConfig.ready(username, email, passw)
        except:
            self.stdout.write('Error in create superuser, waiting 1 second...')
            sleep(1)
         