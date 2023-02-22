from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import temporada
"""
class TemporadaTests(APITestCase):

    def setUp(self):
        self.temporada1 = temporada.objects.create(
            numero_temporada=1, nombre='Temporada 1', 
            descripcion='Descripción temporada 1', foto='foto1.jpg', 
            anio_estreno=2021, cancion='Canción temporada 1', 
            basada_en='Basada en 1')
        self.temporada2 = temporada.objects.create(
            numero_temporada=2, nombre='Temporada 2', 
            descripcion='Descripción temporada 2', foto='foto2.jpg', 
            anio_estreno=2022, cancion='Canción temporada 2', 
            basada_en='Basada en 2')

    def test_get_all_temporadas(self):
        url = reverse('temporada-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_one_temporada(self):
        url = reverse('temporada-detail', args=[self.temporada1.id_temporada])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['numero_temporada'], 1)

    def test_create_temporada(self):
        url = reverse('temporada-list')
        data = {
            'numero_temporada': 3,
            'nombre': 'Temporada 3',
            'descripcion': 'Descripción temporada 3',
            'foto': 'foto3.jpg',
            'anio_estreno': 2023,
            'cancion': 'Canción temporada 3',
            'basada_en': 'Basada en 3'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(temporada.objects.count(), 3)

    def test_update_temporada(self):
        url = reverse('temporada-detail', args=[self.temporada1.id_temporada])
        data = {
            'numero_temporada': 1,
            'nombre': 'Temporada 1 actualizada',
            'descripcion': 'Descripción temporada 1 actualizada',
            'foto': 'foto1_actualizada.jpg',
            'anio_estreno': 2021,
            'cancion': 'Canción temporada 1 actualizada',
            'basada_en': 'Basada en 1 actualizada'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre'], 'Temporada 1 actualizada')

    def test_delete_temporada(self):
        url = reverse('temporada-detail', args=[self.temporada1.id_temporada])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(temporada.objects.count(), 1)
"""