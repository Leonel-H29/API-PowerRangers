import xlrd
# import os
# from dotenv import load_dotenv
from api.db_settings import DBSettings
from colorama import Fore
from datetime import datetime

# load_dotenv()


class CrudCapitulos():

    def __init__(self, DBstt: DBSettings, file_data: str = None) -> None:
        # pass
        self.DB = DBstt  # Inicio una instancia de 'DBSettings'
        self.conn = self.DB.conect_db()
        self.conn.autocommit = True
        self.file = file_data  # Archivo donde extraigo los datos
        self.db_table_name = 'capitulos'
        self.db_table_name_fk = 'temporadas'

    # Funcion para retornar una lista con datos unicos

    def uniq_data(self, dic: dict = {}, list_data: list = []) -> list:
        # Verifica si existe el personaje en la lista
        def check_element_in_list(capitulo: int = 0, temporada: int = 0, list: list = []) -> bool:
            for dictionary in list:
                if capitulo == dictionary["num_cap"] and temporada == dictionary["id_temporada"]:
                    return True
            return False

        try:
            ncap = dic["numero_cap"]
            idtemp = dic["id_temporada"]

            # Verifico si el capitulo esta cargado en la base de datos
            if self.capitulo_exist(cap=ncap, temp=idtemp):
                return list_data

            # Verifico si el capitulo ya se encuentra en la lista
            # Verifica si hay datos en la tabla de la DB
            if (len(list_data) >= 0 and not check_element_in_list(capitulo=ncap, temporada=idtemp, list=list_data)) or self.DB.len_table_db(self.db_table_name) == 0:
                list_data.append(dic)
                return list_data

            # En caso de que no se cumplan ningunas de las condiciones retorno la lista
            return list_data
        except Exception as e:
            print(Fore.RED + "{0}".format(e))
            return list_data

    # Funcion para saber si el capitulo existe

    def capitulo_exist(self, cap: int = 0, temp: int = 0) -> bool:
        query = "SELECT * FROM {0} WHERE numero_cap={1} AND id_temporada={2}".format(
            self.db_table_name, cap, temp)
        return self.DB.exists_tuple(query=query)

    # Funcion para extraer los datos del archivo

    def get_capitulos_file(self):
        if self.DB.len_table_db(table=self.db_table_name_fk) > 0:
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

                query = "SELECT id_temporada FROM {0} WHERE numero_temporada={1};".format(
                    self.db_table_name_fk, col5
                )

                temp = self.DB.get_id(query=query)
                if temp > 0:
                    dic = {
                        "numero_cap": col1,
                        "nombre": col2,
                        "descripcion": col3,
                        "id_temporada": temp
                    }

                # Verifico si el capitulo ya se encuentra registrado
                list_insert = self.uniq_data(dic, list_insert)
            # print(list_insert)
            # print(len(list_insert))
            self.prepare_query_insert(capitulos=list_insert)
        else:
            print(Fore.RED + "Tabla Forenea vacia")

    # Funcion para realizar un insert multiple

    def prepare_query_insert(self, capitulos: list = []) -> None:

        list_values = [
            "({0},'{1}','{2}','{3}','{4}',{5})".format(
                cap["numero_cap"],
                cap["nombre"],
                cap["descripcion"],
                datetime.now(),
                datetime.now(),
                cap["id_temporada"]
            )for cap in sorted(capitulos, key=lambda x: (x["id_temporada"], x["numero_cap"]))
        ]

        if len(list_values) > 0:
            # Ordeno la lista
            query = ",".join(list_values)
            query += ";"

            # print(query)
            self.post_capitulos(capitulos=query)
        else:
            print(Fore.YELLOW + "Lista vacia para insertar datos")

    # Funcion para hacer un insert en la DB

    def post_capitulos(self, capitulos: str = None) -> None:

        query = "INSERT INTO {0} (numero_cap, nombre, descripcion, created, updated, id_temporada) VALUES {1}".format(
            self.db_table_name, capitulos)
        # print(query)
        self.DB.insert_table_query(query=query)

    def put_capitulos(n, data):
        pass
