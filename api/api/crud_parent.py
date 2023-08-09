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
        def db_table_name(self): return self.db_table_name

        @db_table_name.setter
        def db_table_name(self, table_name):
            self.db_table_name = table_name

        @property
        def sheet_file(self): return self.sheet_file

        # def open_file(self):
        # Abro el archivo
        #    openFile = xlrd.open_workbook(self.file)
        # Indico con que hoja voy a trabajar
        #    return openFile.sheet_by_name(self.sheet_file)

        # @property
