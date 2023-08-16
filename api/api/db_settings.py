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
        """Retorna la conexion a la DB."""
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
    def close_conect_db(self) -> None:
        """Finalizo la conexion a la DB."""
        self.conn.close()

    # Retorna la cantidad de registros en una tabla especifica
    def len_table_db_query(self, table: str = None) -> int:
        """
        La función realiza una consulta a la base de datos y
        retorna la cantidad total de registros en una tabla especifica

        ### Args:
            `table (str)`: Nombre de tabla dentro de la base de datos

        ### Returns:
            `int`: Cantidad total de registros de esa tabla

        """
        cursor = self.conn.cursor()
        query = "SELECT COUNT(*) FROM {0};".format(table)
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
        """
        La función se encarga de insertar un registro en la base de datos mediante una consulta

        ### Args:
            `query (str)`: Consulta SQL para realizar la insercion de los datos
        """
        cursor = self.conn.cursor()
        try:
            cursor.execute(query)
            print(Fore.GREEN + "Datos insertados")
        except psycopg2.Error as e:
            print(Fore.RED + f'Error al insertar los datos - {e}')
        finally:
            cursor.close()

    # Exists de una tupla en la base de datos

    def exists_tuple_query(self, query: str = None) -> bool:
        """
        La función realiza una consulta a la base de datos y
        retorna un valor de verdad que determina la existencia o no de una tupla en la base de datos

        ### Args:
            `query (str)`: Consulta SQL para obtener el registro

        ### Returns:
            `bool`: True | False
        """
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

    def get_tuple_query(self, query: str = None) -> list:
        """
        La función realiza una consulta a la base de datos y
        retorna un registro especifico

        ### Args:
            `query (str)`: Consulta SQL para obtener el registro

        ### Returns:
            `list`: Las tuplas que cumplan con las condiciones de la consulta
        """
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

    # Funcion para obtener el ID del registro

    def get_id_query(self, query: str = None) -> int:
        """
        La función realiza una consulta a la base de datos y
        retorna el ID de un registro especifico

        ### Args:
            `query (str)`: Consulta SQL para obtener el ID del registro

        ### Returns:
            `int`: ID del registro
        """
        cursor = self.conn.cursor()
        try:
            if self.exists_tuple_query(query=query):
                cursor.execute(query)
                resultado = cursor.fetchall()
                return int(resultado[0][0])
            return 0
        except psycopg2.Error as e:
            print(Fore.RED + 'Error al realizar la consulta')
            return 0
        finally:
            cursor.close()

    # Funcion para obtener el id de una tabla en especifico
    def get_id_db(self, table: str, params={}) -> int:
        """
        La función se encarga de verificar en base a la tabla enviada por el parametro `table` cual es la consulta
        adecuada para obtener el ID de dicha tabla, tambien se debe tener en cosideracion los parametros `params` para realizar la
        consulta en dicha tabla.

        En caso de que la tabla no exista, se realiza por defecto la consulta a la tabla `actor`

        ### Args:
            - `table (str)`: Nombre de una tabla de la DB
            - `params (dict)`: Los parametros para realizar la consulta en base a la tabla

                Ejs:

                table = actor -> params = { 'nombre_artistico': 'Juan Perez' }

                table = temporada -> params = { 'numero_temporada': 10 }

                table = personaje -> params = { 'nombre_personaje': 'Alpha', 'id_actor': 1 }

                table = capitulos -> params = { 'numero_cap': 10 }

                table = aparecen -> params = { 'id_personaje': 1 , 'id_temporada': 2 }


        ### Returns:
            `int`: El ID de la tabla enviada por parametro
        """
        # Valores para obtener el registro por una columna de la tabla
        actor = params.get('nombre_artistico', '')
        temporada = params.get('numero_temporada', 0)
        personaje = params.get('nombre_personaje', '')
        capitulo = params.get('numero_cap', 0)

        # Valores para obtener el registro por el id de la tabla
        idtemp = params.get('id_temporada', 0)
        idpers = params.get('id_personaje', 0)
        idactor = params.get('id_actor', 0)

        query = {
            "actor": "SELECT id_actor FROM {0} WHERE nombre_artistico='{1}';".format(table, actor),
            "temporadas": "SELECT id_temporada FROM {0} WHERE numero_temporada={1};".format(table, temporada),
            "personajes": "SELECT id_personaje FROM {0} WHERE nombre_personaje='{1}' AND id_actor={2};".format(table, personaje, idactor),
            "capitulos": "SELECT id_capitulo FROM {0} WHERE numero_cap={1} AND id_temporada={2}".format(table, capitulo, idtemp),
            "aparecen": "SELECT id_aparicion FROM {0} WHERE id_personaje={1} AND id_temporada={2}".format(table, idpers, idtemp)
        }
        return self.get_id_query(query=query.get(table, "actor"))

    # Funcion para hacer un insert en la DB segun la tabla
    def post_on_table(self, table: str, values: str) -> None:
        """
        La función se encarga de verificar en base a la tabla enviada por el parametro `table` cual es la consulta
        adecuada para realizar la insercion de los datos en dicha tabla, tambien se debe tener en cosideracion 
        los valores de `values` que indican los valores que se insertan.

        En caso de que la tabla no exista, se realiza por defecto la consulta a la tabla `actor`

        ### Args:
            - `table (str)`: Nombre de una tabla de la DB
            - `values (str)`: Los valores que se insertaran en la base a la tabla
        """
        query = {
            "actor": "INSERT INTO {0} (nombre_actor,nombre_artistico,foto,biografia,created,updated) VALUES {1}".format(table, values),
            "temporadas": "INSERT INTO {0} (numero_temporada, nombre, descripcion, foto, cancion, basada_en, anio_estreno, tematica, created, updated) VALUES {1};".format(table, values),
            "personajes": "INSERT INTO {0} (nombre_personaje, foto, created, updated, id_actor) VALUES {1}".format(table, values),
            "capitulos": "INSERT INTO {0} (numero_cap, titulo, descripcion, created, updated, id_temporada) VALUES {1}".format(table, values),
            "aparecen": "INSERT INTO {0} (rol, descripcion, id_personaje, id_temporada) VALUES {1}".format(table, values),
        }
        self.insert_table_query(query=query.get(table, "actor"))

    # Funcion para lipiar las tablas de las apps
    def clean_db(self) -> None:
        """
        La función realiza una consulta a la base de datos para eliminar los datos
        de cada tabla de la aplicacion
        """

        cursor = self.conn.cursor()
        query = ""

        try:
            for app in self.table_apps:
                query = "DELETE FROM {0}; ".format(app)
                # print(query)
                cursor.execute(query)
                resultado = self.len_table_db_query(app)
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
