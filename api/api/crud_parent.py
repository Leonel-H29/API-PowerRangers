import xlrd
import os
# from dotenv import load_dotenv
from api.settings.production import *
from api.db_settings import DBSettings
# from colorama import Fore
# from datetime import datetime

# load_dotenv()


class CrudParent():

    def __init__(self, DBstt: DBSettings, sheet: str = None, tableName: str = None) -> None:
        # pass
        self.DB = DBstt  # Inicio una instancia de 'DBSettings'
        self.conn = self.DB.conect_db()
        self.conn.autocommit = True
        self.file = FILE_DATA  # Archivo donde extraigo los datos
        self.sheet_file = sheet  # Hoja especifica deñ archivo
        self.db_table_name = tableName  # Nombre de la tabla en la base de datos

        @property
        def file(self): return self.file

        @property
        def db_table_name(self) -> str:
            """
            Funcion GETTER para el nombre de la tabla en la base de datos

            ### Returns:
                `str`: Nombre de la tabla 
            """
            return self.db_table_name

        @db_table_name.setter
        def db_table_name(self, table_name):
            """
            Funcion SETTER para el nombre de la tabla en la base de datos

            ### Args:
                `table_name (str)`: Nombre de la tabla 
            """
            self.db_table_name = table_name

        @property
        def sheet_file(self) -> str:
            """
            Funcion GETTER para el nombre de la hoja de datos

            ### Returns:
                `str`: Nombre de la tabla 
            """
            return self.sheet_file

        # Funcion para realizar un insert multiple

        def __prepare_query_insert(self, list_data: list = []) -> None:
            """
            La funcion que encarga de ordenar los registros para poder realizar la consulta en la base de datos

            ### Args:
                `list_data (list)`: Lista de los valores a insertar en la base de datos
            """
            pass

        # Funcion para extraer los datos del archivo
        def get_data_file(self):
            """
            La funcion se encarga de extraer todos los datos de la hoja
            """
            pass

         # Funcion para retornar una lista con datos unicos
        def __uniq_data(self, dic: dict = {}, list_data: list = []) -> list:
            """
            La funcion se encarga de controlar que los datos extraidos dentro de la lista `list_data` sean unicos, es decir, datos no repetidos dentro de
            la lista, como asi que no esten ya cargados en la base de datos

            ### Args:
                - `dic (dict)`: Diccionario con los valores extraidos en cada fila de la hoja
                - `list_data`: Lista de datos a cargarse en la base de datos

            ### Returns:
                `list`: Lista de datos unicos
            """
            return list_data
