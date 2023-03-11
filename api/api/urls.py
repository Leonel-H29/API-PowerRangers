from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth.views import LogoutView
from Temporadas.urls import router as routerTemp
from Actor.urls import router as routerAct
from Capitulos.urls import router as routerCap 
from User.urls import router as routerUser

class DefaultRouter(routers.DefaultRouter):
    """
    Extends `DefaultRouter` class to add a method for
    extending url routes from another router.
    """
    def extend(self, router):
        """
        Extend the routes with url routes of the passed in router.
 
        Args:
             router: SimpleRouter instance containing route definitions.
        """
        self.registry.extend(router.registry)


router = DefaultRouter()
router.extend(routerTemp)
router.extend(routerAct)
router.extend(routerCap)
router.extend(routerUser)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include(router.urls)),    
    #path("", include("Temporadas.urls")),
    #path("", include("Actor.urls")),
    #path("", include("Capitulos.urls"))
]
