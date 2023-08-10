from time import sleep
import os
from django.core.management.base import BaseCommand
from api.settings.production import *
from api.db_settings import DBSettings

# Importo los cruds
from Actor.crud_actores import CrudActores
from Actor.crud_aparecen import CrudAparecen
from Actor.crud_personajes import CrudPersonajes
from Capitulos.crud_capitulos import CrudCapitulos
from Temporadas.crud_temporadas import CrudTemporadas

# from django.db import connection
from django.db.utils import OperationalError


class Command(BaseCommand):
    # help = 'Wait for database connection'

    def handle(self, *args, **options):

        DB = DBSettings(
            user=DB_USER, passw=DB_PASSWORD,
            db=DB_NAME, port=DB_PORT, host=DB_HOST
        )

        try:
            if DB.conect_db():
                # Clases independientes
                Actor = CrudActores(
                    DBstt=DB, sheet='Actores', tableName='actor'
                )
                Temp = CrudTemporadas(
                    DBstt=DB, sheet='Temporadas', tableName='temporadas'
                )
                # Clases dependientes
                Cap = CrudCapitulos(
                    DBstt=DB, sheet='Capitulos', tableName='capitulos'
                )
                Pers = CrudPersonajes(
                    DBstt=DB, sheet='Personajes', tableName='personajes'
                )
                Apar = CrudAparecen(
                    DBstt=DB, sheet='Personajes', tableName='aparecen'
                )

                tablas: list = [Actor, Temp, Cap, Pers, Apar]

                # print(Fore.GREEN + 'Conexion exitosa')

                self.stdout.write('Loadding data to database...')
                for x in tablas:
                    self.stdout.write(
                        '----{0}: ...'.format(x.db_table_name.capitalize())
                    )
                    x.get_data_file()
                    sleep(1)

            DB.close_conect_db()

        except OperationalError:
            self.stdout.write(self.style.ERROR(
                'Error in connection to database'
            ))
