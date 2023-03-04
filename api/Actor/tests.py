from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import actor

class ActoresTest(APITestCase):
    #Inicializacion de la clase
    def setUp(self):
        self.url = '/actores/'
        self.actor1 = actor.objects.create(
            nombre_actor='Leo Herrera',
            nombre_artistico='Leo Herrera',
            foto='http://www.developerpe.com/programaci%C3%B3n/testing-con-python-y-django/',
            biografia='http://www.developerpe.com/programaci%C3%B3n/testing-con-python-y-django/'
        )
        
    #Test para evaluar si se trae todos los actores correctamente
    def test_get_all_actores(self):
        response = self.client.get(self.url)
        #print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
    
    #Test para evaluar si se trae a un actor correctamente
    def test_get_one_actor(self):
        url = self.url + str(self.actor1.id_actor) + '/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre_actor'], self.actor1.nombre_actor)
    
    #Test para evaluar si el actor se crea correctamente
    def test_create_actor(self):
        data = {
            'nombre_actor':'Pablo Rago',
            'nombre_artistico':'Pablo Rago',
            'foto':'http://www.developerpe.com/programaci%C3%B3n/testing-con-python-y-django/',
            'biografia':'http://www.developerpe.com/programaci%C3%B3n/testing-con-python-y-django/'
        }
        response = self.client.post(self.url, data, format='json')
        #print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['nombre_actor'], data['nombre_actor'])
        self.assertEqual(actor.objects.count(), 3)
    
    #Test para evaluar si el actor se actualiza correctamente
    def test_update_actor(self):
        data = {
            'nombre_actor':'Pablo Perez Lopez',
            'nombre_artistico':'Pablo Perez Lopez',
            'foto':'http://www.developerpe.com/programaci%C3%B3n/testing-con-python-y-django/',
            'biografia':'http://www.developerpe.com/programaci%C3%B3n/testing-con-python-y-django/'
        }
        url = self.url + str(self.actor1.id_actor) + '/'
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre_actor'], data['nombre_actor'])
    
    #Test para evaluar si el actor se elimina correctamente
    def test_delete_actor(self):
        url = self.url + str(self.actor1.id_actor) + '/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(actor.objects.count(), 1)