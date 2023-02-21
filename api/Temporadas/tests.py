from django.test import TestCase

# Create your tests here.
import pytest

from .models import temporada

@pytest.fixture
def temporada_ejemplo():
    return temporada.objects.create(
        numero_temporada=1,
        nombre='Temporada de prueba',
        descripcion='Descripción de temporada de prueba',
        foto='http://example.com/temporada_de_prueba.jpg',
        anio_estreno=2022,
        cancion='Canción de prueba',
        basada_en='Una obra literaria de prueba',
    )

def test_get_temporada(client, temporada_ejemplo):
    response = client.get(f'/temporadas/{temporada_ejemplo.id_temporada}/')
    assert response.status_code == 200
    assert response.json()['nombre'] == 'Temporada de prueba'

def test_post_temporada(client):
    data = {
        'numero_temporada': 2,
        'nombre': 'Otra temporada de prueba',
        'descripcion': 'Descripción de otra temporada de prueba',
        'foto': 'http://example.com/otra_temporada_de_prueba.jpg',
        'anio_estreno': 2023,
        'cancion': 'Otra canción de prueba',
        'basada_en': 'Otra obra literaria de prueba',
    }
    response = client.post('/temporadas/', data=data)
    assert response.status_code == 201
    assert temporada.objects.filter(nombre='Otra temporada de prueba').exists()

def test_put_temporada(client, temporada_ejemplo):
    data = {
        'nombre': 'Temporada de prueba actualizada',
        'descripcion': 'Nueva descripción de temporada de prueba',
    }
    response = client.put(f'/temporadas/{temporada_ejemplo.id_temporada}/', data=data)
    assert response.status_code == 200
    assert response.json()['nombre'] == 'Temporada de prueba actualizada'
    temporada_ejemplo.refresh_from_db()
    assert temporada_ejemplo.descripcion == 'Nueva descripción de temporada de prueba'

def test_delete_temporada(client, temporada_ejemplo):
    response = client.delete(f'/temporadas/{temporada_ejemplo.id_temporada}/')
    assert response.status_code == 204
    assert not temporada.objects.filter(id_temporada=temporada_ejemplo.id_temporada).exists()

