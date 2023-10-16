import xlrd
import os
# from dotenv import load_dotenv
from api.settings.production import *
from api.db_settings import DBSettings
from abc import abstractclassmethod
# from colorama import Fore
# from datetime import datetime

# load_dotenv()


class CrudParent():
    @abstractclassmethod
    def __init__(self, DBstt: DBSettings, sheet: str = None, tableName: str = None) -> None:
        # pass
        self.__DB = DBstt  # Inicio una instancia de 'DBSettings'
        self.__conn = self.__DB.conect_db()
        self.__conn.autocommit = True
        self.__file = FILE_DATA  # Archivo donde extraigo los datos
        self.__sheet_file = sheet  # Hoja especifica del archivo
        self.__db_table_name = tableName  # Nombre de la tabla en la base de datos

    """
    GETTERS & SETTERS
    """
    @property
    def file(self):
        """
        Funcion GETTER para el nombre del archivo de donde se extre los datos

        ### Returns:
            `str`: Nombre del fichero
        """
        return self.__file

    @property
    def DB(self) -> DBSettings:
        """
        Funcion GETTER el objeto de la clase `DBSettings`

        ### Returns:
            `DBSettings`: Objeto de la clase `DBSettings`
        """
        return self.__DB

    @property
    def db_table_name(self) -> str:
        """
        Funcion GETTER para el nombre de la tabla en la base de datos

        ### Returns:
            `str`: Nombre de la tabla 
        """
        return self.__db_table_name

    @property
    def sheet_file(self) -> str:
        """
        Funcion GETTER para el nombre de la hoja de datos

        ### Returns:
            `str`: Nombre de la tabla 
        """
        return self.__sheet_file

    # Funcion para abrir el archivo

    def open_file(self):
        """
            La funcion se encarga de abrir el archivo y retorna los datos de una hoja especifica del archivo

            ### Returns:
            `xlrd`: Datos de la hoja del archivo 
        """
        # Abro el archivo
        openFile = xlrd.open_workbook(self.file)
        # Indico con que hoja voy a trabajar
        sheet = openFile.sheet_by_name(self.sheet_file)

        return sheet

    # Funcion para realizar un insert multiple

    @abstractclassmethod
    def __prepare_query_insert(self, list_data: list = []) -> None:
        """
        La funcion que encarga de ordenar los registros para poder realizar la consulta en la base de datos

        ### Args:
            `list_data (list)`: Lista de los valores a insertar en la base de datos
        """
        pass

     # Funcion para extraer los datos del archivo

    @abstractclassmethod
    def get_data_file(self):
        """
        La funcion se encarga de extraer todos los datos de la hoja
        """
        pass

    # Funcion para retornar una lista con datos unicos

    @abstractclassmethod
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
