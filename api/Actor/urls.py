#from django.conf.urls import url
from django.urls import path, include
from . import views
#from django.conf import settings
#from  django.conf.urls.static import static

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'actores', views.ActoresViewSet, basename='actores')
router.register(r'aparecen', views.AparecenViewSet, basename='aparecen')
router.register(r'personajes', views.PersonajesViewSet, basename='personajes')


urlpatterns = [
    path('', include(router.urls)),
]