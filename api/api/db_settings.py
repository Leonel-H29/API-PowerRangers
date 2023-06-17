import os
import psycopg2
from colorama import Fore
from api.settings.base import *


class DBSettings():

    def __init__(self, host: str = None, user: str = None, passw: str = None, db: str = None, port: str = None) -> None:
        self.host = host
        self.user = user
        self.password = passw
        self.database = db
        self.port = port

        self.table_apps = ['aparecen', 'personajes',
                           'capitulos', 'actor', 'temporadas']

        if self.conect_db():
            self.conn = self.conect_db()
            self.conn.autocommit = True

    # Retorna la conexion a la DB.

    def conect_db(self):
        return (
            psycopg2.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port
            )
        )

    # Finalizo la conexion a la DB.
    def close_conect_db(self) -> None: self.conn.close()

    # Retorna la cantidad de registros en una tabla especifica
    def len_table_db(self, table: str = None) -> int:
        cursor = self.conn.cursor()
        query = "SELECT COUNT(*) FROM {0};".format(table)
        # print(query)
        try:
            cursor.execute(query)
            # Extraigo el resultado de la tupla dentro de una lista
            resultado = cursor.fetchall()[0][0]
            return resultado
        except psycopg2.Error as e:
            print(Fore.RED + 'Error al realizar la consulta')
            return 0
        finally:
            cursor.close()
            # self.conn.close()

    # Elimina la base de datos
    def drop_db(self):
        pass

    # Insert en una tabla de la base de datos

    def insert_table_query(self, query: str = None) -> None:
        cursor = self.conn.cursor()
        try:
            cursor.execute(query)
            print(Fore.GREEN + "Datos insertados")
        except psycopg2.Error as e:
            print(Fore.RED + f'Error al insertar los datos - {e}')
        finally:
            cursor.close()

    # Exists de una tupla en la base de datos

    def exists_tuple(self, query: str = None) -> bool:
        cursor = self.conn.cursor()
        try:
            cursor.execute(query)
            resultado = cursor.fetchall()
            return len(resultado) > 0
        except psycopg2.Error as e:
            print(Fore.RED + 'Error al realizar la consulta')
            return False
        finally:
            cursor.close()

    # Funcion para obtener el registro

    def get_tuple(self, query: str = None) -> list:
        cursor = self.conn.cursor()
        try:
            cursor.execute(query)
            resultado = cursor.fetchall()
            return resultado
        except psycopg2.Error as e:
            print(Fore.RED + 'Error al realizar la consulta')
            return []
        finally:
            cursor.close()

    # Funcion para obtener el registro

    def get_id(self, query: str = None) -> int:
        cursor = self.conn.cursor()
        try:
            if self.exists_tuple(query=query):
                cursor.execute(query)
                resultado = cursor.fetchall()
                return int(resultado[0][0])
            return 0
        except psycopg2.Error as e:
            print(Fore.RED + 'Error al realizar la consulta')
            return 0
        finally:
            cursor.close()

    # Funcion para lipiar las tablas de las apps
    def clean_db(self) -> None:
        cursor = self.conn.cursor()
        query = ""

        try:
            for app in self.table_apps:
                query = "DELETE FROM {0}; ".format(app)
                # print(query)
                cursor.execute(query)
                resultado = self.len_table_db(app)
                if resultado == 0:
                    print(Fore.GREEN + "Cantidad de registros en '{0}' :{1}".format(
                        app, resultado)
                    )
                else:
                    print("Hubo un error al realizar la consulta")
        except psycopg2.Error as e:
            print(Fore.RED + "{0}".format(str(e)))
        finally:
            cursor.close()
