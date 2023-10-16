
import xlrd
from api.db_settings import DBSettings
from api.crud_parent import CrudParent

from colorama import Fore


class CrudAparecen(CrudParent):
    def __init__(self, DBstt: DBSettings, sheet: str = None, tableName: str = None) -> None:
        super().__init__(DBstt, sheet, tableName)
        self.db_table_name_fk1 = 'temporadas'
        self.db_table_name_fk2 = 'personajes'
        self.db_table_name_fk3 = 'actor'

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
            idpers = dic["id_personaje"]
            idtemp = dic["id_temporada"]

            exists_in_list = any(
                registro["id_personaje"] == idpers and
                registro["id_temporada"] == idtemp
                for registro in list_data
            )

            # Verifico si la aparicion esta cargada en la base de datos
            # Verifico si la aparicion ya se encuentra en la lista
            if self.DB.get_id_db(self.db_table_name, params={'id_personaje': idpers, 'id_temporada': idtemp}) > 0 or exists_in_list:
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
        if self.DB.get_len_table(table=self.db_table_name_fk1) > 0 and self.DB.get_len_table(table=self.db_table_name_fk2) > 0:

            sheet = self.open_file()

            list_insert = []

            for i in range(1, sheet.nrows):
                col1 = sheet.cell_value(i, 0)  # Nombre del Personaje
                col2 = int(sheet.cell_value(i, 1))  # Numero de temporada
                col3 = sheet.cell_value(i, 2)  # Rol
                col4 = sheet.cell_value(i, 3)  # Descripcion
                # col5 = sheet.cell_value(i, 4)  # Foto
                col6 = sheet.cell_value(i, 5)  # Nombre del actor

                actor = self.DB.get_id_db(
                    self.db_table_name_fk3,
                    params={'nombre_artistico': col6}
                )

                temp = self.DB.get_id_db(
                    self.db_table_name_fk1,
                    params={'numero_temporada': col2}
                )

                pers = self.DB.get_id_db(
                    self.db_table_name_fk2,
                    params={'nombre_personaje': col1, 'id_actor': actor}
                )

                if temp > 0 and pers > 0:
                    dic = {
                        "rol": col3,
                        "descripcion": col4,
                        "id_personaje": pers,
                        "id_temporada": temp
                    }

                    # Verifico si el aparicion ya se encuentra registrado
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
            list_values = [
                (
                    apar["rol"],
                    apar["descripcion"],
                    apar["id_personaje"],
                    apar["id_temporada"]

                )for apar in sorted(list_data, key=lambda x: (x["id_temporada"], x["id_personaje"]))
            ]
            self.DB.post_on_table(table=self.db_table_name, values=list_values)
        else:
            print(Fore.YELLOW + "Lista vacia para insertar datos")
