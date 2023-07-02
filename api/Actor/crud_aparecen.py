
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

    def uniq_data(self, dic: dict = {}, list_data: list = []) -> list:

        try:
            idtemp = dic["id_personaje"]
            idtemp = dic["id_temporada"]

            exists_in_list = any(
                registro["id_personaje"] == idtemp and
                registro["id_temporada"] == idtemp
                for registro in list_data
            )

            # Verifico si el aparicion esta cargado en la base de datos
            # Verifico si el aparicion ya se encuentra en la lista
            if self.aparicion_exist(pers=idtemp, temp=idtemp) or exists_in_list:
                return list_data

            list_data.append(dic)
            return list_data

        except Exception as e:
            print(Fore.RED + "{0}".format(e))
            return list_data

    # Funcion para saber si el aparicion existe

    def aparicion_exist(self, pers: int = 0, temp: int = 0) -> bool:
        query = "SELECT * FROM {0} WHERE id_personaje={1} AND id_temporada={2}".format(
            self.db_table_name, pers, temp)
        return self.DB.exists_tuple(query=query)

    # Funcion para extraer los datos del archivo

    def get_apariciones_file(self):
        if self.DB.len_table_db(table=self.db_table_name_fk1) > 0 and self.DB.len_table_db(table=self.db_table_name_fk2) > 0:
            # Abro el archivo
            openFile = xlrd.open_workbook(self.file)
            # Indico con que hoja voy a trabajar
            sheet = openFile.sheet_by_name(self.sheet_file)

            list_insert = []

            for i in range(1, sheet.nrows):
                col1 = sheet.cell_value(i, 0)  # Nombre del Personaje
                col2 = int(sheet.cell_value(i, 1))  # Numero de temporada
                col3 = sheet.cell_value(i, 2)  # Rol
                col4 = sheet.cell_value(i, 3)  # Descripcion
                # col5 = sheet.cell_value(i, 4)  # Foto
                col6 = sheet.cell_value(i, 5)  # Nombre del actor

                query1 = "SELECT id_temporada FROM {0} WHERE numero_temporada={1};".format(
                    self.db_table_name_fk1, col2
                )
                subquery = "SELECT id_actor FROM {0} WHERE nombre_artistico='{1}';".format(
                    self.db_table_name_fk3, col6
                )
                query2 = "SELECT id_personaje FROM {0} WHERE nombre_personaje='{1}';".format(
                    self.db_table_name_fk2, self.DB.get_id(query=subquery)
                )

                temp = self.DB.get_id(query=query1)
                pers = self.DB.get_id(query=query2)
                if temp > 0 and pers > 0:
                    dic = {
                        "rol": col3,
                        "descripcion": col4,
                        "id_personaje": pers,
                        "id_temporada": temp
                    }

                    # Verifico si el aparicion ya se encuentra registrado
                    list_insert = self.uniq_data(dic, list_insert)
            # print(list_insert)
            # print(len(list_insert))
            self.prepare_query_insert(apariciones=list_insert)
        else:
            print(Fore.RED + "Tabla Forenea vacia")

    # Funcion para realizar un insert multiple

    def prepare_query_insert(self, apariciones: list = []) -> None:

        list_values = [
            "('{0}','{1}',{2},{3})".format(
                apar["rol"],
                apar["descripcion"],
                apar["id_personaje"],
                apar["id_temporada"]

            )for apar in sorted(apariciones, key=lambda x: (x["id_temporada"], x["id_personaje"]))
        ]

        if len(list_values) > 0:
            # Ordeno la lista
            query = ",".join(list_values)
            query += ";"

            # print(query)
            self.post_apariciones(apariciones=query)
        else:
            print(Fore.YELLOW + "Lista vacia para insertar datos")

    # Funcion para hacer un insert en la DB

    def post_apariciones(self, apariciones: str = None) -> None:

        query = "INSERT INTO {0} (rol, descripcion, id_personaje, id_temporada) VALUES {1}".format(
            self.db_table_name, apariciones)
        # print(query)
        self.DB.insert_table_query(query=query)

    def put_apariciones(n, data):
        pass
