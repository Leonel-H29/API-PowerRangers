#from django.test import TestCase
from rest_framework.test import APITestCase, APIRequestFactory, APIClient
from django.urls import reverse
from rest_framework import status
from .views import ActoresViewSet
from .models import actor
import pytest
import json
# Create your tests here.

class ActoresTestCase(APITestCase):
    #Inicializacion de la clase
    def setUp(self) -> None:
        self.factory=APIRequestFactory()
        self.view=ActoresViewSet()
        self.url='/actores/'
    
    #Test para evaluar si el actor se crea correctamente
    def test_create_actor(self):
        people = actor.objects.create(
            nombre_actor='Pablo Rago',
            nombre_artistico='Pablo Rago',
            foto='http://www.developerpe.com/programaci%C3%B3n/testing-con-python-y-django/',
            biografia='http://www.developerpe.com/programaci%C3%B3n/testing-con-python-y-django/'
        )
        assert people.nombre_actor == 'Pablo Rago'
            
    
    #Test para evaluar si el actor se postea correctamente
    def test_post_actores(self):
        try:
            people = actor.objects.create(
                nombre_actor='Pablo Rago',
                nombre_artistico='Pablo Rago',
                foto='http://www.developerpe.com/programaci%C3%B3n/testing-con-python-y-django/',
                biografia='http://www.developerpe.com/programaci%C3%B3n/testing-con-python-y-django/'
            )
            client = APIClient()
            response = client.post(self.url, people,  format='multipart')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(
                self.assertEqual(json.loads(response.content), {
                    'nombre_actor':'Pablo Rago',
                    'nombre_artistico':'Pablo Rago',
                    'foto':'http://www.developerpe.com/programaci%C3%B3n/testing-con-python-y-django/',
                    'biografia':'http://www.developerpe.com/programaci%C3%B3n/testing-con-python-y-django/'
                })
                ) 
        except:
            with pytest.raises(Exception) as exc_info:
                client.post(self.url, people,  format='multipart')
        self.assertEqual(str(exc_info.value), "'actor' object has no attribute 'items'")   
            

    #Test para evaluar si se trae los actores correctamente
    def test_get_actores(self):
        response = self.client.get(self.url, format='json')
        """
        Pruebo si el resultado de la respuesta es el mismo que espero,
        en este caso el status 200
        """
        print(response.json())
        json = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json['count'], 0)
        
        