import xlrd
import os
from dotenv import load_dotenv
from db_settings import DBSettings
from colorama import Fore
from datetime import datetime
import psycopg2

load_dotenv()


class CrudActores():

    def __init__(self) -> None:
        # pass
        self.DB = DBSettings()  # Inicio una instancia de 'DBSettings'
        self.conn = self.DB.conect_db()
        self.conn.autocommit = True
        self.file = os.getenv('FILE_DATA')  # Archivo donde extraigo los datos
        self.db_table_name = 'actor'

    # Funcion para retornar una lista con datos unicos

    def uniq_data(self, dic: dict = {}, list_data: list = []) -> list:
        # Extaigo el 'nombre_artistico' del diccionario
        try:
            nombre = dic["nombre_artistico"]

            # Verifico si el actor esta cargado en la base de datos
            if self.actor_exists(nombre):
                return list_data

            if len(list_data) > 0:
                for data in list_data:
                    if nombre == data["nombre_artistico"]:
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

        # return list_data

    # Funcion para extraer los datos del archivo

    def get_actores_file(self):

        # Abro el archivo
        openFile = xlrd.open_workbook(self.file)
        # Indico con que hoja voy a trabajar
        sheet = openFile.sheet_by_name("Actores")

        list_insert = []

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
                "biografia": col4,
                "created": datetime.now(),
                "updated": datetime.now()
            }

            # Verifico si el actor ya se encuentra registrado
            list_insert = self.uniq_data(dic, list_insert)

        self.prepare_query_insert(list_insert)

    # Funcion para saber si el actor existe

    def actor_exists(self, name: str = None) -> bool:
        query = "SELECT * FROM {0} WHERE nombre_artistico='%s';".format(
            self.db_table_name, name)
        return self.DB.exists_tuple(query=query)

    # Funcion para obtener el registro del actor por el nombre artistico

    def get_actor_by_nombre_artistico(self, name: str):
        cursor = self.conn.cursor()
        query = "SELECT * FROM {0} WHERE nombre_artistico='{1}';".format(
            self.db_table_name, name
        )
        # print(query)
        try:
            cursor.execute(query)
            resultado = cursor.fetchall()
            return resultado
        except psycopg2.Error as e:
            print(Fore.RED + 'Error al realizar la consulta')
            return []
        finally:
            cursor.close()
            # self.conn.close()

    # Funcion para realizar un insert multiple

    def prepare_query_insert(self, actores: list = []) -> None:

        list_values = []

        list_values = [
            "('{0}','{1}','{2}','{3}','{4}','{5}'),".format(
                actor["nombre_actor"],
                actor["nombre_artistico"],
                actor["foto"],
                actor["biografia"],
                actor["created"],
                actor["updated"]
            )for actor in actores
        ]

        if len(list_values) > 0:
            # Ordeno la lista
            list_values = sorted(list_values)
            query = ",".join(list_values)
            query += ";"

            # print(list_values)
            self.post_actores(actores=query)
        else:
            print(Fore.YELLOW + "Lista vacia para insertar datos")

    # Funcion para hacer un insert en la DB

    def post_actores(self, actores: str = None) -> None:
        query = "INSERT INTO actor(nombre_actor,nombre_artistico,foto,biografia,created,updated) VALUES "
        query += actores
        self.DB.insert_table_query(query=query)

    def put_actores(n, data):
        pass
