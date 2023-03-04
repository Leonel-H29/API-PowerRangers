from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import temporada

class TemporadaTests(APITestCase):
    #Inicializacion de la clase
    def setUp(self):
        self.url = '/temporadas/'
        self.temporada1 = temporada.objects.create(
            numero_temporada=1, 
            nombre='Temporada 1', 
            descripcion='Descripción temporada 1', 
            foto='foto1.jpg', 
            anio_estreno=2021, 
            cancion='Canción temporada 1', 
            basada_en='Basada en 1',
            tematica='dinosaurios')
        self.temporada2 = temporada.objects.create(
            numero_temporada=2, nombre='Temporada 2', 
            descripcion='Descripción temporada 2', foto='foto2.jpg', 
            anio_estreno=2022, cancion='Canción temporada 2', 
            basada_en='Basada en 2', tematica='policias')

    #Test para evaluar si se trae todos las temporadas correctamente
    def test_get_all_temporadas(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    #Test para evaluar si se trae a una temporada correctamente
    def test_get_one_temporada(self):
        url = self.url + str(self.temporada1.id_temporada) + '/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['numero_temporada'], 1)


    #Test para evaluar si la temporada se crea correctamente
    def test_create_temporada(self):
        data = {
            'numero_temporada': 3,
            'nombre': 'Temporada 3',
            'descripcion': 'Descripción temporada 3',
            'foto': 'foto3.jpg',
            'anio_estreno': 2023,
            'cancion': 'Canción temporada 3',
            'basada_en': 'Basada en 3',
            'tematica': 'viajes en el tiempo'
        }
        response = self.client.post(self.url, data=data, format='json')
        print("Creacion:", response.status_code)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(temporada.objects.count(), 3)


    #Test para evaluar si la temporada se actualiza correctamente
    def test_update_temporada(self):
        data = {
            'numero_temporada': 1,
            'nombre': 'Temporada 1 actualizada',
            'descripcion': 'Descripción temporada 1 actualizada',
            'foto': 'foto1_actualizada.jpg',
            'anio_estreno': 2021,
            'cancion': 'Canción temporada 1 actualizada',
            'basada_en': 'Basada en 1 actualizada',
            'tematica': 'viajes en el tiempo'
        }
        url = self.url + str(self.temporada1.id_temporada)  + '/'
        response = self.client.put(url, data=data, format='json')
        print("Actualizacion:" ,response.status_code)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre'], 'Temporada 1 actualizada')

        
    #Test para evaluar si la temporada se elimina correctamente
    def test_delete_temporada(self):
        url = self.url + str(self.temporada2.id_temporada) + '/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(temporada.objects.count(), 1)