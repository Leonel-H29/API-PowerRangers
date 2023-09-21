import xlrd

from api.db_settings import DBSettings
from api.crud_parent import CrudParent

from colorama import Fore
from datetime import datetime

# load_dotenv()


class CrudTemporadas(CrudParent):

    def __init__(self, DBstt: DBSettings, sheet: str = None, tableName: str = None) -> None:
        super().__init__(DBstt, sheet, tableName)
        # print(self.file)

    # Funcion para extraer los datos del archivo

    def get_data_file(self):
        """
            La funcion se encarga de extraer todos los datos de la hoja
        """
        # Abro el archivo
        openFile = xlrd.open_workbook(self.file)
        # Indico con que hoja voy a trabajar
        sheet = openFile.sheet_by_name(self.sheet_file)

        list_insert: list = []

        for i in range(1, sheet.nrows):
            col1 = int(sheet.cell_value(i, 0))  # Ntemporada
            col2 = sheet.cell_value(i, 1)  # Nombre
            col3 = sheet.cell_value(i, 2)  # Descripcion
            col4 = sheet.cell_value(i, 3)  # Foto
            col5 = sheet.cell_value(i, 4)  # Cancion
            col6 = sheet.cell_value(i, 5)  # Basada en
            col7 = int(sheet.cell_value(i, 6))  # Año de estreno
            col8 = sheet.cell_value(i, 7)  # Tematica

            # exist = exist_temporada(col1)
            dic = {
                "numero_temporada": col1,
                "nombre": col2,
                "descripcion": col3,
                "foto": col4,
                "cancion": col5,
                "basada_en": col6,
                "anio_estreno": col7,
                "tematica": col8
            }
            # Verifico si la temporada ya se encuentra registrada
            list_insert = self.uniq_data(dic=dic, list_data=list_insert)
        # print(list_insert)

        self.prepare_query_insert(list_data=list_insert)

    # Funcion para retornar una lista con datos unicos

    def uniq_data(self, dic: dict = {}, list_data: list = []) -> list:
        """
            La funcion se encarga de controlar que los datos extraidos dentro de la lista `list_data` sean unicos, es decir, datos no repetidos dentro de
            la lista, como asi que no esten ya cargados en la base de datos

            ### Args:
                - `dic (dict)`: Diccionario con los valores extraidos en cada fila de la hoja
                - `list_data`: Lista de datos a cargarse en la base de datos

            ### Returns:
                `list`: Lista de datos unicos
        """
        # Extaigo el 'numero_temporada' del diccionario
        try:
            ntemp = dic["numero_temporada"]
            exists_in_list = any(
                registro["numero_temporada"] == ntemp for registro in list_data
            )

            # Verifico si la temporada esta cargada en la base de datos
            # Verifico si la temporada ya se encuentra en la lista
            if self.DB.get_id_db(self.db_table_name, params={'numero_temporada': ntemp}) > 0 or exists_in_list:
                return list_data

            list_data.append(dic)
            return list_data
        except Exception as e:
            print(Fore.RED + "{0}".format(e))
            return list_data

    # Funcion para realizar un insert multiple

    def prepare_query_insert(self, list_data: list = []) -> None:
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
                    temp["numero_temporada"],
                    temp["nombre"],
                    temp["descripcion"],
                    temp["foto"],
                    temp["cancion"],
                    temp["basada_en"],
                    temp["anio_estreno"],
                    temp["tematica"],
                    datetime.now(),
                    datetime.now()
                )for temp in sorted(list_data, key=lambda x: (x["anio_estreno"]))
            ]
            self.DB.post_on_table(table=self.db_table_name, values=list_values)
        else:
            print(Fore.YELLOW + "Lista vacia para insertar datos")
