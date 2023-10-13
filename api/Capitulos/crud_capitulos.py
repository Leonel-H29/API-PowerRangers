import xlrd
from api.db_settings import DBSettings
from api.crud_parent import CrudParent
from colorama import Fore
from datetime import datetime


class CrudCapitulos(CrudParent):

    def __init__(self, DBstt: DBSettings, sheet: str = None, tableName: str = None) -> None:
        super().__init__(DBstt, sheet, tableName)
        self.db_table_name_fk = 'temporadas'

    # Funcion para retornar una lista con datos unicos

    def __uniq_data(self, dic: dict = {}, list_data: list = []) -> list:
        """
            La funcion se encarga de controlar que los datos extraidos dentro de la lista `list_data` sean unicos, es decir, datos no repetidos dentro de
            la lista, como asi que no esten ya cargados en la base de datos

            ### Args:
                - `dic (dict)`: Diccionario con los valores extraidos en cada fila de la hoja
                - `list_data`: Lista de datos a cargarse en la base de datos

            ### Returns:
                `list`: Lista de datos unicos
        """
        try:
            ncap = dic["numero_cap"]
            idtemp = dic["id_temporada"]

            exists_in_list = any(
                registro["numero_cap"] == ncap and
                registro["id_temporada"] == idtemp
                for registro in list_data
            )

            # Verifico si el capitulo esta cargado en la base de datos
            # Verifico si el capitulo ya se encuentra en la lista
            # if self.capitulo_exist(cap=ncap, temp=idtemp) or exists_in_list:
            if self.DB.get_id_db(self.db_table_name, params={'numero_cap': ncap, 'id_temporada': idtemp}) > 0 or exists_in_list:
                return list_data

            list_data.append(dic)
            return list_data

        except Exception as e:
            print(Fore.RED + "{0}".format(e))
            return list_data

    # Funcion para extraer los datos del archivo

    def get_data_file(self):
        """
            La funcion se encarga de extraer todos los datos de la hoja
        """
        if self.DB.len_table_db_query(table=self.db_table_name_fk) > 0:
            # Abro el archivo
            openFile = xlrd.open_workbook(self.file)
            # Indico con que hoja voy a trabajar
            sheet = openFile.sheet_by_name(self.sheet_file)

            list_insert = []

            for i in range(1, sheet.nrows):
                col1 = int(sheet.cell_value(i, 0))  # Numero del episodio
                col2 = sheet.cell_value(i, 1)  # Titulo
                col3 = sheet.cell_value(i, 2)  # Descripcion
                # col4 = sheet.cell_value(i,3) #Temporada
                col5 = int(sheet.cell_value(i, 4))  # Numero de temporada

                temp = self.DB.get_id_db(
                    self.db_table_name_fk,
                    params={'numero_temporada': col5}
                )
                if temp > 0:
                    dic = {
                        "numero_cap": col1,
                        "titulo": col2,
                        "descripcion": col3,
                        "id_temporada": temp
                    }

                # Verifico si el capitulo ya se encuentra registrado
                list_insert = self.__uniq_data(dic, list_insert)
            # print(list_insert)
            # print(len(list_insert))
            self.__prepare_query_insert(list_data=list_insert)
        else:
            print(Fore.RED + "Tabla Forenea vacia")

    # Funcion para realizar un insert multiple

    def __prepare_query_insert(self, list_data: list = []) -> None:
        """
            La funcion que encarga de ordenar los registros para poder realizar la consulta en la base de datos

            ### Args:
                `list_data (list)`: Lista de los valores a insertar en la base de datos
        """
        # Controlo si hay datos para insertar
        if len(list_data) > 0:
            # Ordeno los valores a insertar en la base de datos
            list_values = [
                (
                    cap["numero_cap"],
                    cap["titulo"],
                    cap["descripcion"],
                    datetime.now(),
                    datetime.now(),
                    cap["id_temporada"]
                )for cap in sorted(list_data, key=lambda x: (x["id_temporada"], x["numero_cap"]))
            ]
            self.DB.post_on_table(table=self.db_table_name, values=list_values)
        else:
            print(Fore.YELLOW + "Lista vacia para insertar datos")
