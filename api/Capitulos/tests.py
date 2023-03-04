from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from Capitulos.models import capitulo
from Temporadas.models import temporada
from Capitulos.serializers import CapitulosSerializer

class CapitulosTest(APITestCase):
    #Inicializacion de la clase
    def setUp(self):
        self.url = '/capitulos/'
        
        self.temporada1 = temporada.objects.create(
            numero_temporada=1, nombre='Temporada 1', 
            descripcion='Descripción temporada 1', foto='foto1.jpg', 
            anio_estreno=2021, cancion='Canción temporada 1', 
            basada_en='Basada en 1', tematica='Policias')

        self.capitulo1 = capitulo.objects.create(
            numero_cap=1,
            nombre='El Inicio',
            descripcion=' ',
            temporada=self.temporada1
        )
        self.valid_payload  = {
            "numero_cap": 2,
            "nombre": "Nuevo capítulo",
            "descripcion": "Nueva descripción",
            "temporada": self.temporada1.id_temporada
        }
       
        
    #Test para evaluar si se trae todos los capitulos correctamente
    def test_get_all_capitulos(self):
        response = self.client.get(self.url)
        #print(response.data)
        capitulos = capitulo.objects.all()
        serializer = CapitulosSerializer(capitulos, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #self.assertEqual(response.data, serializer.data)
        #self.assertEqual(len(response.data), 2)
    
    #Test para evaluar si se trae a un capitulo correctamente
    def test_get_one_capitulo(self):
        url = self.url + str(self.capitulo1.id_capitulo) + '/'
        response = self.client.get(url)
        
        one_cap = capitulo.objects.get(id_capitulo=self.capitulo1.id_capitulo)
        serializer = CapitulosSerializer(one_cap)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
        #self.assertEqual(response.data['nombre'], self.capitulo1.nombre)
        #self.assertEqual(response.data['temporada'], self.temporada1.id_temporada)
    
    #Test para evaluar si el capitulo se crea correctamente
    def test_create_capitulo(self):
        
        response = self.client.post(self.url, data=self.valid_payload , format='json')
        #print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #self.assertEqual(response.data['nombre'], data['nombre'])
        #self.assertEqual(response.data['temporada'],self.temporada1.id_temporada)

        #self.assertEqual(capitulo.objects.count(), 3)
    
    #Test para evaluar si el capitulo se actualiza correctamente
    def test_update_capitulo(self):

        url = self.url + str(self.capitulo1.id_capitulo) + '/'
        response = self.client.put(url, data=self.valid_payload , format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #self.assertEqual(response.data['nombre'], data['nombre'])
    
    #Test para evaluar si el capitulo se elimina correctamente
    def test_delete_capitulo(self):
        url = self.url + str(self.capitulo1.id_capitulo) + '/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(capitulo.objects.count(), 1)