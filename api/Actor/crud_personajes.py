import xlrd
# import os
# from dotenv import load_dotenv
from api.db_settings import DBSettings
from colorama import Fore
from datetime import datetime

# load_dotenv()


class CrudPersonajes():
    def __init__(self, DBstt: DBSettings, file_data: str = None) -> None:
        # pass
        self.DB = DBstt  # Inicio una instancia de 'DBSettings'
        self.conn = self.DB.conect_db()
        self.conn.autocommit = True
        self.file = file_data  # Archivo donde extraigo los datos
        self.sheet_file = 'Personajes'
        self.db_table_name = 'personajes'
        self.db_table_name_fk = 'actor'

    # Funcion para retornar una lista con datos unicos

    def uniq_data(self, dic: dict = {}, list_data: list = []) -> list:
        # Verifica si existe el personaje en la lista
        def check_element_in_list(personaje: str = None, actor: int = 0, list: list = []) -> bool:
            for dictionary in list:
                if personaje == dictionary["nombre_personaje"] and actor == dictionary["id_actor"]:
                    return True
            return False
        try:
            pers = dic["nombre_personaje"]
            idactor = dic["id_actor"]

            # Verifico si el personaje esta cargado en la base de datos
            if self.personaje_exist(pers=pers, actor=idactor):
                return list_data

            # Verifico si el personaje ya se encuentra en la lista
            # Verifica si hay datos en la tabla de la DB
            if (len(list_data) >= 0 and check_element_in_list(personaje=pers, actor=idactor, list=list_data)) or self.DB.len_table_db(self.db_table_name) == 0:
                list_data.append(dic)
                return list_data

            # En caso de que no se cumplan ningunas de las condiciones retorno la lista
            return list_data
        except Exception as e:
            print(Fore.RED + "{0}".format(str(e)))
            return list_data

    # Funcion para saber si el personaje existe

    def personaje_exist(self, pers: str = None, actor: int = 0) -> bool:
        query = "SELECT * FROM {0} WHERE nombre_personaje='{1}' AND id_actor={2}".format(
            self.db_table_name, pers, actor)
        return self.DB.exists_tuple(query=query)

    # Funcion para extraer los datos del archivo
    def get_personajes_file(self):
        if self.DB.len_table_db(table=self.db_table_name_fk) > 0:
            # Abro el archivo
            openFile = xlrd.open_workbook(self.file)
            # Indico con que hoja voy a trabajar
            sheet = openFile.sheet_by_name(self.sheet_file)

            list_insert: list = []

            for i in range(1, sheet.nrows):
                col1 = sheet.cell_value(i, 0)  # Nombre del Personaje
                # col2 = int(sheet.cell_value(i, 1))  # Numero de temporada
                # col3 = sheet.cell_value(i, 2)  # Rol
                # col4 = sheet.cell_value(i, 3)  # Descripcion
                col5 = sheet.cell_value(i, 4)  # Foto
                col6 = sheet.cell_value(i, 5)  # Nombre del actor

                query = "SELECT id_actor FROM {0} WHERE nombre_artistico='{1}';".format(
                    self.db_table_name_fk, col6)

                actor = self.DB.get_id(query=query)

                if actor > 0:
                    dic = {
                        "nombre_personaje": col1,
                        "foto": col5,
                        "id_actor": actor
                    }

                    # Verifico si el actor ya se encuentra registrado
                    # print(type(list_insert))
                    list_insert = self.uniq_data(
                        dic=dic, list_data=list_insert
                    )
            # print(list_insert)
            self.prepare_query_insert(personajes=list_insert)
        else:
            print(Fore.RED + "Tabla Forenea vacia")

    def put_personajes(personajes):
        pass

    def prepare_query_insert(self, personajes: list = []) -> None:

        list_values = [
            "('{0}','{1}','{2}','{3}',{4})".format(
                cap["nombre_personaje"],
                cap["foto"],
                datetime.now(),
                datetime.now(),
                cap["id_actor"]
            )for cap in sorted(personajes, key=lambda x: (x["nombre_personaje"], x["id_actor"]))
        ]

        if len(list_values) > 0:
            # Ordeno la lista
            query = ",".join(list_values)
            query += ";"

            # print(list_values)
            self.post_personajes(personajes=query)
        else:
            print(Fore.YELLOW + "Lista vacia para insertar datos")

    # Funcion para hacer un insert en la DB

    def post_personajes(self, personajes: str = None) -> None:
        query = "INSERT INTO {0} (nombre_personaje, foto, created, updated, id_actor) VALUES {1}".format(
            self.db_table_name, personajes)
        self.DB.insert_table_query(query=query)
