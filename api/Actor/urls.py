#from django.conf.urls import url
from django.urls import path, include
from . import views
#from django.conf import settings
#from  django.conf.urls.static import static

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'actores', views.ActoresViewSet, basename='actores')
#router.register(r'mutuales', views.MutualesViewSet, basename='mutuales')
# router.register(r'servicio_mutual', views.ServiciosMutualViewSet, basename='servicios_mutuales')
#router.register(r'planes', views.PlanesViewSet, basename='planes')
#router.register(r'beneficios', views.BeneficiosViewSet, basename='beneficios')

urlpatterns = [
    path('', include(router.urls)),
]