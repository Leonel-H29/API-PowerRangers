import xlrd
# import os
# from dotenv import load_dotenv
from api.db_settings import DBSettings
from colorama import Fore
from datetime import datetime

# load_dotenv()


class CrudTemporadas():

    def __init__(self, DBstt: DBSettings, file_data: str = None) -> None:
        # pass
        self.DB = DBstt  # Inicio una instancia de 'DBSettings'
        self.conn = self.DB.conect_db()
        self.conn.autocommit = True
        self.file = file_data  # Archivo donde extraigo los datos
        self.sheet_file = 'Temporadas'
        self.db_table_name = 'temporadas'
        # print(self.file)

    # Funcion para saber si la temporada existe

    def temporada_exist(self, temp: int = 0) -> bool:
        query = "SELECT * FROM {0} WHERE numero_temporada={1}".format(
            self.db_table_name, temp
        )
        return self.DB.exists_tuple(query=query)

    # Funcion para extraer los datos del archivo

    def get_temporadas_file(self):
        # Abro el archivo
        openFile = xlrd.open_workbook(self.file)
        # Indico con que hoja voy a trabajar
        sheet = openFile.sheet_by_name(self.sheet_file)

        list_insert: list = []

        for i in range(1, sheet.nrows):
            col1 = int(sheet.cell_value(i, 0))  # Ntemporada
            col2 = sheet.cell_value(i, 1)  # Nombre
            col3 = sheet.cell_value(i, 2)  # Descripcion
            col4 = sheet.cell_value(i, 3)  # Foto
            col5 = sheet.cell_value(i, 4)  # Cancion
            col6 = sheet.cell_value(i, 5)  # Basada en
            col7 = int(sheet.cell_value(i, 6))  # Año de estreno
            col8 = sheet.cell_value(i, 7)  # Tematica

            # exist = exist_temporada(col1)
            dic = {
                "numero_temporada": col1,
                "nombre": col2,
                "descripcion": col3,
                "foto": col4,
                "cancion": col5,
                "basada_en": col6,
                "anio_estreno": col7,
                "tematica": col8
            }
            # Verifico si la temporada ya se encuentra registrada
            list_insert = self.uniq_data(dic=dic, list_data=list_insert)
        # print(list_insert)

        self.prepare_query_insert(list_insert)

    # Funcion para retornar una lista con datos unicos

    def uniq_data(self, dic: dict = {}, list_data: list = []) -> list:
        # Extaigo el 'numero_temporada' del diccionario
        try:
            ntemp = dic["numero_temporada"]
            exists_in_list = any(
                registro["numero_temporada"] == ntemp for registro in list_data
            )

            # Verifico si el actor esta cargado en la base de datos
            # Verifico si la temporada ya se encuentra en la lista
            if self.temporada_exist(ntemp) or exists_in_list:
                return list_data

            list_data.append(dic)
            return list_data
        except Exception as e:
            print(Fore.RED + "{0}".format(e))
            return list_data

    # Funcion para realizar un insert multiple

    def prepare_query_insert(self, temporadas: list = []) -> None:

        list_values = [
            "({0},'{1}','{2}','{3}','{4}','{5}',{6},'{7}','{8}','{9}')".format(
                temp["numero_temporada"],
                temp["nombre"],
                temp["descripcion"],
                temp["foto"],
                temp["cancion"],
                temp["basada_en"],
                temp["anio_estreno"],
                temp["tematica"],
                datetime.now(),
                datetime.now()
            )for temp in temporadas
        ]

        if len(list_values) > 0:
            # Ordeno la lista
            list_values = sorted(list_values)
            query = ",".join(list_values)
            query += ";"

            # print(list_values)
            # print(query)
            self.post_temporadas(temporadas=query)
        else:
            print(Fore.YELLOW + "Lista vacia para insertar datos")

    # Funcion para hacer un insert en la DB

    def post_temporadas(self, temporadas: str = None) -> None:
        query = "INSERT INTO {0} (numero_temporada, nombre, descripcion, foto, cancion, basada_en, anio_estreno, tematica, created, updated) VALUES {1}".format(
            self.db_table_name, temporadas)

        self.DB.insert_table_query(query=query)

    def put_temporadas(n, data):
        pass
