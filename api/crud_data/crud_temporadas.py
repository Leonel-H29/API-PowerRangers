import xlrd
import os
from dotenv import load_dotenv
from conect_db import conect_db
from colorama import Fore
from datetime import datetime
import psycopg2

class CrudTemporadas():
    load_dotenv()
    conn = conect_db()
    conn.autocommit = True
    
    def exist_temporada(temp):
        cursor = conn.cursor()
        query = "SELECT * FROM temporadas WHERE numero_temporada={0}".format(temp)
        #query = "SELECT * FROM temporadas WHERE numero_temporada=100".format(temp)  
        try:
            cursor.execute(query)
            resultado = cursor.fetchall()
            if resultado != []:
                return True
            return False
        except:
            #raise Exception('Error al insertar los datos')
            print(Fore.RED + 'Error al buscar la temporada')
        cursor.close()
        return False
    
    def get_temporadas() : 
        file = os.getenv('FILE_DATA')
        openFile = xlrd.open_workbook(file)
        #Indico con que hoja voy a trabajar
        sheet = openFile.sheet_by_name("Temporadas")

        #Cantidad de filas
        #print(Fore.GREEN +"Cantidad de filas: {0}".format(sheet.nrows))

        list_insert = []
    

        for i in range(1, sheet.nrows):
            col1 = int(sheet.cell_value(i,0)) #Ntemporada
            col2 = sheet.cell_value(i,1) #Nombre
            col3 = sheet.cell_value(i,2) #Descripcion
            col4 = sheet.cell_value(i,3) #Foto
            col5 = sheet.cell_value(i,4) #Cancion
            col6 = sheet.cell_value(i,5) #Basada en
            col7 = int(sheet.cell_value(i,6)) #Año de estreno
            col8 = sheet.cell_value(i,7) #Tematica
            fyh=datetime.now()
            #print("({0},'{1}','{2}','{3}','{4}','{5}',{6},{7});".format(col1,col2,col3,col4,col5.replace('"', '*'),col6,col7, col8))
        
            exist = exist_temporada(col1)
            #print(exist)
            #print(len(exist))
        
            if exist==True:
                set = "nombre='{0}',descripcion='{1}',foto='{2}',cancion='{3}',basada_en='{4}',anio_estreno={5},tematica='{6}',updated='{7}'".format(col2,col3,col4,col5.replace('"', '*'),col6,col7,col8,fyh)
                put_temporadas(col1, set)
            else:
                values = "({0},'{1}','{2}','{3}','{4}','{5}',{6},'{7}','{8}','{9}'),".format(col1,col2,col3,col4,col5.replace('"', '*'),col6,col7, col8,fyh,fyh)
                list_insert.append(values)
                #print("Inserto datos")   
    
        if len(list_insert) > 0:
            #Busco el ultimo elemeto de la lista
            index = len(list_insert) - 1
            #print(index)
    
            #Le quito el ',' al ultimo registro y luego lo reemplazo por ';'
            list_insert[index] = list_insert[index][0:len(list_insert[index])-1]
            list_insert[index] += ';'
    
            #print(list_insert[index])
            post_temporadas(list_insert)
        else:
            print(Fore.RED + "Lista vacia para insertar datos")
    
    def post_temporadas(temporadas):
        cant: int = len(temporadas)
        cursor = conn.cursor()
        query = "INSERT INTO actor(nombre_actor,nombre_artistico,foto,biografia,created,updated) VALUES "  
        try:
            for i in range(0, cant):
                query += temporadas[i]
            #print(query)
            cursor.execute(query)
            print(Fore.GREEN + "Datos insertados")
        except  psycopg2.Error as e:
            print(Fore.RED + f'Error al insertar los datos - {e}')
        cursor.close()
    
   
    def put_temporadas(n, data):
        cursor = conn.cursor()
        #print(data)
        query = "UPDATE temporadas SET {0} WHERE numero_temporada={1}".format(data,n)  
        #print(query)
        try:
            cursor.execute(query)
            print(Fore.GREEN + "Datos actualizados")
        except:
            print(Fore.RED + 'Error al actualizar los datos')
        cursor.close()