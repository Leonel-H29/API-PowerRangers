# import os
from dotenv import load_dotenv
from colorama import Fore
from db_settings import DBSettings
from crud_actores import CrudActores
from time import sleep


if __name__ == "__main__":
    # Inico instancias
    DB = DBSettings()
    Actor = CrudActores()

    if DB.conect_db():
        # print(DB.conect_db())

        print(Fore.GREEN + 'Conexion exitosa')
        # print(DB.len_table_db('actor'))

        # Clases independientes
        # print(Fore.RESET + "----Temporadas: ")
        # GetTemporadas()
        print(Fore.RESET + "----Actores: ")
        # GetActores()
        Actor.get_actores_file()
        sleep(1)

        # Clases dependientes
        # print(Fore.RESET + "----Capitulos: ")
        # GetCapitulos()
        # print(Fore.RESET + "----Personajes: ")
        # GetPersonajes()
        # print(Fore.RESET + "----Aparecen: ")
        # GetAparecen()
        DB.close_conect_db()

    else:
        print(Fore.RED + 'Error al conectar a la base de datos')
