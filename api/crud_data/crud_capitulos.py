import xlrd
import os
from dotenv import load_dotenv
from db_settings import DBSettings
from colorama import Fore
from datetime import datetime
import psycopg2

load_dotenv()


class CrudCapitulos():

    def __init__(self) -> None:
        # pass
        self.DB = DBSettings()  # Inicio una instancia de 'DBSettings'
        self.conn = self.DB.conect_db()
        self.conn.autocommit = True
        self.file = os.getenv('FILE_DATA')  # Archivo donde extraigo los datos
        self.db_table_name = 'capitulos'

    def capitulo_exist(self, cap: int = 0, temp: int = 0) -> bool:
        subquery = "SELECT id_temporada FROM temporadas WHERE numero_temporada={0}".format(
            temp)
        query = "SELECT * FROM capitulos WHERE numero_cap={0} AND id_temporada=({1})".format(
            cap, subquery)
        return self.DB.exists_tuple(query=query)

    def get_capitulos():
        file = os.getenv('FILE_DATA')
        openFile = xlrd.open_workbook(file)
        # Indico con que hoja voy a trabajar
        sheet = openFile.sheet_by_name("Capitulos")

        # Cantidad de filas
        # print(sheet.nrows)

        list_insert = []

        for i in range(1, sheet.nrows):
            col1 = int(sheet.cell_value(i, 0))  # Numero del episodio
            col2 = sheet.cell_value(i, 1)  # Titulo
            col3 = sheet.cell_value(i, 2)  # Descripcion
            # col4 = sheet.cell_value(i,3) #Temporada
            col5 = int(sheet.cell_value(i, 4))  # Numero de temporada
            fyh = datetime.now()

            exist = existCapitulo(col1, col5)
            subquery = "SELECT id_temporada FROM temporadas WHERE numero_temporada={0}".format(
                col5)
            if exist == True:
                set = "numero_cap={0},nombre='{1}',descripcion='{2}',updated='{3}',id_temporada=({4}) ".format(
                    col1, col2, col3, fyh, subquery)
                put_capitulos(col1, subquery, set)
            else:
                values = "({0},'{1}','{2}','{3}','{4}',({5})),".format(
                    col1, col2, col3, fyh, fyh, subquery)
                list_insert.append(values)

        if len(list_insert) > 0:
            # Busco el ultimo elemeto de la lista
            index = len(list_insert) - 1
            # print(index)

            # Le quito el ',' al ultimo registro y luego lo reemplazo por ';'
            list_insert[index] = list_insert[index][0:len(
                list_insert[index])-1]
            list_insert[index] += ';'

            # print(list_insert[index])
            post_capitulos(list_insert)
        else:
            print(Fore.RED + "Lista vacia para insertar datos")
        # return list_insert

    def post_capitulos(capitulos):
        cant: int = len(capitulos)
        cursor = conn.cursor()
        query = "INSERT INTO capitulos (numero_cap, nombre, descripcion, created, updated, id_temporada) VALUES "
        try:
            for i in range(0, cant):
                query += capitulos[i]
            cursor.execute(query)
            print(Fore.GREEN + "Datos insertados")
        except psycopg2.Error as e:
            # raise Exception('Error al insertar los datos')
            print(Fore.RED + f'Error al insertar los datos - {e}')
        cursor.close()

    def put_capitulos(n, data):
        cursor = conn.cursor()
        # print(data)
        query = "UPDATE capitulos SET {0} WHERE numero_cap={1} AND id_temporada=({2})".format(
            data, n, temp)
        # print(query)
        try:
            cursor.execute(query)
            print(Fore.GREEN + "Datos actualizados")
        except:
            print(Fore.RED + 'Error al actualizar los datos')
        cursor.close()
