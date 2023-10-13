import xlrd
# import os
# from dotenv import load_dotenv
from api.db_settings import DBSettings
from api.crud_parent import CrudParent
from colorama import Fore
from datetime import datetime

# load_dotenv()


class CrudActores(CrudParent):

    def __init__(self, DBstt: DBSettings, sheet: str = None, tableName: str = None) -> None:
        super().__init__(DBstt, sheet, tableName)

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
        try:
            # Extaigo el 'nombre_artistico' del diccionario
            nombre = dic["nombre_artistico"]
            exists_in_list = any(
                registro["nombre_artistico"] == nombre for registro in list_data
            )

            # Verifico si el actor esta cargado en la base de datos
            # Verifico si el actor ya se encuentra en la lista
            if self.DB.get_id_db(self.db_table_name, params={'nombre_artistico': nombre}) > 0 or exists_in_list:
                return list_data

            list_data.append(dic)
            return list_data
        except Exception as e:
            print(Fore.RED + "{0}".format(e))
            return list_data

    # Funcion para extraer los datos del archivo

    def get_data_file(self):
        """
            La funcion se encarga de extraer todos los datos de la hoja
        """
        # Abro el archivo
        openFile = xlrd.open_workbook(self.file)
        # Indico con que hoja voy a trabajar
        sheet = openFile.sheet_by_name(self.sheet_file)

        list_insert: list = []

        for i in range(1, sheet.nrows):
            col1 = sheet.cell_value(i, 0)  # Nombre artistico del actor
            col2 = sheet.cell_value(i, 1)  # Nombre real del actor
            col3 = sheet.cell_value(i, 2)  # Foto
            col4 = sheet.cell_value(i, 3)  # Link de la biografia
            # print(type(col1), type(col2), type(col3), type(col4))

            dic = {
                "nombre_artistico": col1,
                "nombre_actor": col2,
                "foto": col3,
                "biografia": col4
            }
            # Verifico si el actor ya se encuentra registrado
            list_insert = self.__uniq_data(dic=dic, list_data=list_insert)
        # print(list_insert)

        self.__prepare_query_insert(list_data=list_insert)

    # Funcion para realizar un insert multiple

    def __prepare_query_insert(self, list_data: list = []) -> None:
        """
            La funcion que encarga de ordenar los registros para poder realizar la consulta en la base de datos

            ### Args:
                `list_data (list)`: Lista de los valores a insertar en la base de datos
        """
        # Controlo si hay datos para insertar
        if len(list_data) > 0:
            # Ordeno los valores a insertar en la base de datos
            list_values = [
                (
                    actor["nombre_actor"],
                    actor["nombre_artistico"],
                    actor["foto"],
                    actor["biografia"],
                    datetime.now(),
                    datetime.now()
                )for actor in sorted(list_data, key=lambda x: (x["nombre_actor"]))
            ]
            self.DB.post_on_table(table=self.db_table_name, values=list_values)
        else:
            print(Fore.YELLOW + "Lista vacia para insertar datos")
