import xlrd
import os
from dotenv import load_dotenv
from conect_db import conect_db
from colorama import Fore
from datetime import datetime
import psycopg2

class CrudPersonajes():
    load_dotenv()
    conn = conect_db()
    conn.autocommit = True
    
    def get_personajes() : 
        file = os.getenv('FILE_DATA')
        openFile = xlrd.open_workbook(file)
        #Indico con que hoja voy a trabajar
        sheet = openFile.sheet_by_name("Personajes")

        list_insert = []

        for i in range(1, sheet.nrows):
            col1 = sheet.cell_value(i,0) #Nombre del Personaje
            col2 = int(sheet.cell_value(i,1)) #Numero de temporada
            col3 = sheet.cell_value(i,2) #Rol
            col4 = sheet.cell_value(i,3) #Descripcion
            col5 = sheet.cell_value(i,4) #Foto 
            col6 = sheet.cell_value(i,5) #Nombre del actor
            fyh=datetime.now()
            
        subquery = "SELECT id_actor FROM actor WHERE nombre_artistico='{0}' LIMIT 1".format(col6)
        exist = existPersonaje(col1,subquery)
        if exist==True:
            #print(getIdPersonaje(col1,subquery))
            #pass
            set = "nombre_personaje='{0}', foto='{1}', updated='{2}', id_actor=({3})".format(col1,col5,fyh,subquery)
            put_personajes(getIdPersonaje(col1,subquery),set)
        else:   
            values = "('{0}','{1}','{2}','{3}',({4})),".format(col1,col5,fyh,fyh,subquery)
            #print(values)
            list_insert.append(values)
    
        if len(list_insert) > 0:
            #Busco el ultimo elemeto de la lista
            index = len(list_insert) - 1
            
            #Le quito el ',' al ultimo registro y luego lo reemplazo por ';'
            list_insert[index] = list_insert[index][0:len(list_insert[index])-1]
            list_insert[index] += ';'
    
            post_personajes(list_insert)
        else:
            print(Fore.RED + "Lista vacia para insertar datos")
    
    def put_personajes(personajes):
        cursor = conn.cursor()
        #print(data)
        query = "UPDATE personajes SET {0} WHERE id_personaje={1};".format(data,id)  
        #print(query)
        try:
            #pass
            cursor.execute(query)
            print(Fore.GREEN + "Datos actualizados")
        except:
            print(Fore.RED + 'Error al actualizar los datos')
        cursor.close()
    
    def post_personajes(n, data):
        cant: int = len(personajes)
        cursor = conn.cursor()
        query = "INSERT INTO personajes (nombre_personaje, foto, created, updated, id_actor) VALUES "  
        try:
            for i in range(0, cant):
                query += personajes[i]
            cursor.execute(query)
            print(Fore.GREEN + "Datos insertados")   
        except psycopg2.Error as e:
            #raise Exception('Error al insertar los datos')
            print(Fore.RED + f'Error al insertar los datos - {e}')
        cursor.close()