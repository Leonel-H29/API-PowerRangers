import xlrd
import os
from dotenv import load_dotenv
from db_settings import DBSettings
from colorama import Fore
from datetime import datetime

load_dotenv()


class CrudCapitulos():

    def __init__(self) -> None:
        # pass
        self.DB = DBSettings()  # Inicio una instancia de 'DBSettings'
        self.conn = self.DB.conect_db()
        self.conn.autocommit = True
        self.file = os.getenv('FILE_DATA')  # Archivo donde extraigo los datos
        self.db_table_name = 'capitulos'
        self.db_table_name_fk = 'temporadas'

    # Funcion para retornar una lista con datos unicos

    def uniq_data(self, dic: dict = {}, list_data: list = []) -> list:
        try:
            ncap = dic["numero_cap"]
            idtemp = dic["id_temporada"]

            # Verifico si el actor esta cargado en la base de datos
            if self.capitulo_exist(cap=ncap, temp=idtemp):
                return list_data

            if len(list_data) > 0:
                for data in list_data:
                    if ncap == data["numero_cap"] and idtemp == data["id_temporada"]:
                        return list_data

                return list_data.append(dic)

            # Verifica si hay datos en la tabla de la DB
            if self.DB.len_table_db(self.db_table_name) == 0:
                return list_data.append(dic)

            # En caso de que no se cumplan ningunas de las condiciones retorno la lista
            return list_data
        except Exception:
            print(Fore.RED + "Dictionary not will be null")
            return list_data

    # Funcion para saber si el capitulo existe

    def capitulo_exist(self, cap: int = 0, temp: int = 0) -> bool:
        subquery = "SELECT id_temporada FROM {0} WHERE numero_temporada={1}".format(
            self.db_table_name_fk, temp)
        query = "SELECT * FROM {0} WHERE numero_cap={1} AND id_temporada=({2})".format(
            self.db_table_name, cap, subquery)
        return self.DB.exists_tuple(query=query)

    # Funcion para extraer los datos del archivo

    def get_capitulos_file(self):
        # Abro el archivo
        openFile = xlrd.open_workbook(self.file)
        # Indico con que hoja voy a trabajar
        sheet = openFile.sheet_by_name("Capitulos")

        list_insert = []

        for i in range(1, sheet.nrows):
            col1 = int(sheet.cell_value(i, 0))  # Numero del episodio
            col2 = sheet.cell_value(i, 1)  # Titulo
            col3 = sheet.cell_value(i, 2)  # Descripcion
            # col4 = sheet.cell_value(i,3) #Temporada
            col5 = int(sheet.cell_value(i, 4))  # Numero de temporada

            query = "SELECT * FROM {0} WHERE numero_temporada={1}".format(
                self.db_table_name_fk, col5
            )

            temp = self.DB.get_by_id(query=query)
            if temp:
                dic = {
                    "numero_cap": col1,
                    "nombre": col2,
                    "descripcion": col3,
                    "created": datetime.now(),
                    "updated": datetime.now(),
                    "id_temporada": int(temp[0][0])
                }

            # Verifico si el actor ya se encuentra registrado
            list_insert = self.uniq_data(dic, list_insert)
        self.prepare_query_insert()

    # Funcion para realizar un insert multiple

    def prepare_query_insert(self, capitulos: list = []) -> None:

        list_values = []

        list_values = [
            "({0},'{1}','{2}','{3}','{4}',{5}),".format(
                cap["numero_cap"],
                cap["nombre"],
                cap["descripcion"],
                cap["created"],
                cap["updated"],
                cap["id_temporada"]
            )for cap in sorted(capitulos, key=lambda x: (x["id_temporada"], x["numero_cap"]))
        ]

        if len(list_values) > 0:
            # Ordeno la lista
            query = ",".join(list_values)
            query += ";"

            # print(list_values)
            self.post_capitulos(capitulos=query)
        else:
            print(Fore.YELLOW + "Lista vacia para insertar datos")

    # Funcion para hacer un insert en la DB

    def post_capitulos(self, capitulos: str = None) -> None:

        query = "INSERT INTO capitulos (numero_cap, nombre, descripcion, created, updated, id_temporada) VALUES "
        query += capitulos
        self.DB.insert_table_query(query=query)

    def put_capitulos(n, data):
        pass
