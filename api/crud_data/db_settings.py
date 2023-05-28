import os
from dotenv import load_dotenv
import psycopg2
from colorama import Fore
import psycopg2

# FILE_ENV= '.env'
# load_dotenv(FILE_ENV)
load_dotenv()


class DBSettings():

    def __init__(self) -> None:
        self.host = os.getenv('DB_HOST')
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD'),
        self.database = os.getenv('DB_NAME')
        self.port = os.getenv('DB_PORT')

        if self.conect_db():
            self.conn = self.conect_db()
            self.conn.autocommit = True
        # else:
        # print(Fore.GREEN + 'Conexion exitosa')

    # Retorna la conexion a la DB.
    def conect_db(self) -> None:
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
        # cursor = self.conn.cursor()
        # query = "DROP DATABASE {0};".format(self.database)
        # print(query)
        # try:
        # cursor.execute(query)
        # resultado = cursor.fetchall()
        # print(Fore.GREEN + 'Base de datos eliminada exitosamente!')
        # except psycopg2.Error as e:
        # print(Fore.RED + 'Error al eliminar la base de datos')
        # finally:
        # cursor.close()
        # self.conn.close()

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
