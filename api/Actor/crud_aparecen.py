
import xlrd
import os
from dotenv import load_dotenv
# from conect_db import conect_db
from colorama import Fore
from datetime import datetime
import psycopg2


class CrudAparecen():
    pass


"""
    load_dotenv()
    conn = conect_db()
    conn.autocommit = True

    def get_apariciones():
        file = os.getenv('FILE_DATA')
        openFile = xlrd.open_workbook(file)
        # Indico con que hoja voy a trabajar
        sheet = openFile.sheet_by_name("Personajes")

        list_insert = []

        for i in range(1, sheet.nrows):
            col1 = sheet.cell_value(i, 0)  # Nombre del Personaje
            col2 = int(sheet.cell_value(i, 1))  # Numero de temporada
            col3 = sheet.cell_value(i, 2)  # Rol
            col4 = sheet.cell_value(i, 3)  # Descripcion

            IDPer = getIdPersonaje(col1)
            IDTemp = getIdTemporada(col2)
            # col5 = sheet.cell_value(i,4) #Foto
            # col6 = sheet.cell_value(i,5) #Nombre del actor
            # fyh=datetime.now()
            exist = existAparicion(IDPer, IDTemp)
            if exist == True:
                # pass
                set = "rol='{0}', descripcion='{1}', id_personaje={2}, id_temporada={3}".format(
                    col3, col4, IDPer, IDTemp)
                put_aparecen(getIdAparicion(IDPer, IDTemp), set)
            else:
                values = "('{0}','{1}',{2},{3}),".format(
                    col3, col4, IDPer, IDTemp)
                # print(values)
                list_insert.append(values)

        if len(list_insert) > 0:
            # Busco el ultimo elemeto de la lista
            index = len(list_insert) - 1

            # Le quito el ',' al ultimo registro y luego lo reemplazo por ';'
            list_insert[index] = list_insert[index][0:len(
                list_insert[index])-1]
            list_insert[index] += ';'

            post_aparecen(list_insert)
        else:
            print(Fore.RED + "Lista vacia para insertar datos")

    def post_apariciones(apariciones):
        cant: int = len(apariciones)
        cursor = conn.cursor()
        query = "INSERT INTO aparecen (rol, descripcion, id_personaje, id_temporada) VALUES "
        try:
            for i in range(0, cant):
                query += apariciones[i]
            cursor.execute(query)
            print(Fore.GREEN + "Datos insertados")
        except psycopg2.Error as e:
            # raise Exception('Error al insertar los datos')
            print(Fore.RED + f'Error al insertar los datos - {e}')
        cursor.close()

    def put_apariciones(n, data):
        cursor = conn.cursor()
        # print(data)
        query = "UPDATE aparecen SET {0} WHERE id_aparicion={1};".format(
            data, id)
        # print(query)
        try:
            # pass
            cursor.execute(query)
            print(Fore.GREEN + "Datos actualizados")
        except:
            print(Fore.RED + 'Error al actualizar los datos')
        cursor.close()
"""
