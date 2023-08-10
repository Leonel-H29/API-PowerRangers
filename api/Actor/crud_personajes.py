import xlrd
from api.db_settings import DBSettings
from api.crud_parent import CrudParent
from colorama import Fore
from datetime import datetime

# load_dotenv()


class CrudPersonajes(CrudParent):
    def __init__(self, DBstt: DBSettings, sheet: str = None, tableName: str = None) -> None:
        super().__init__(DBstt, sheet, tableName)
        self.db_table_name_fk = 'actor'

    # Funcion para retornar una lista con datos unicos

    def uniq_data(self, dic: dict = {}, list_data: list = []) -> list:
        try:
            pers = dic["nombre_personaje"]
            idactor = dic["id_actor"]

            exists_in_list = any(
                registro["nombre_personaje"] == pers
                # and registro["id_actor"] == idactor
                for registro in list_data
            )

            # Verifico si el personaje esta cargado en la base de datos
            # Verifico si el personaje ya se encuentra en la lista
            if self.DB.get_id_db(self.db_table_name, params={'nombre_personaje': pers, 'id_actor': idactor}) > 0 or exists_in_list:
                return list_data

            list_data.append(dic)
            return list_data

        except Exception as e:
            print(Fore.RED + "{0}".format(str(e)))
            return list_data

    # Funcion para extraer los datos del archivo

    def get_data_file(self):
        if self.DB.len_table_db_query(table=self.db_table_name_fk) > 0:
            # Abro el archivo
            openFile = xlrd.open_workbook(self.file)
            # Indico con que hoja voy a trabajar
            sheet = openFile.sheet_by_name(self.sheet_file)

            list_insert: list = []

            for i in range(1, sheet.nrows):
                col1 = sheet.cell_value(i, 0)  # Nombre del Personaje
                # col2 = int(sheet.cell_value(i, 1))  # Numero de temporada
                # col3 = sheet.cell_value(i, 2)  # Rol
                # col4 = sheet.cell_value(i, 3)  # Descripcion
                col5 = sheet.cell_value(i, 4)  # Foto
                col6 = sheet.cell_value(i, 5)  # Nombre del actor

                actor = self.DB.get_id_db(
                    self.db_table_name_fk,
                    params={
                        'nombre_artistico': col6
                    }
                )

                if actor > 0:
                    dic = {
                        "nombre_personaje": col1,
                        "foto": col5,
                        "id_actor": actor
                    }

                    # Verifico si el actor ya se encuentra registrado
                    # print(type(list_insert))
                    list_insert = self.uniq_data(
                        dic=dic, list_data=list_insert
                    )
            # print(list_insert)
            self.prepare_query_insert(personajes=list_insert)
        else:
            print(Fore.RED + "Tabla Forenea vacia")

    def put_personajes(personajes):
        pass

    def prepare_query_insert(self, personajes: list = []) -> None:

        list_values = [
            "('{0}','{1}','{2}','{3}',{4})".format(
                cap["nombre_personaje"],
                cap["foto"],
                datetime.now(),
                datetime.now(),
                cap["id_actor"]
            )for cap in sorted(personajes, key=lambda x: (x["nombre_personaje"], x["id_actor"]))
        ]

        if len(list_values) > 0:
            # Ordeno la lista
            query = ",".join(list_values)
            query += ";"

            # print(list_values)
            self.DB.post_on_table(table=self.db_table_name, values=query)
        else:
            print(Fore.YELLOW + "Lista vacia para insertar datos")
