from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth.views import LogoutView
from Temporadas.urls import router as routerTemp
from Actor.urls import router as routerAct
from Capitulos.urls import router as routerCap 
from User.urls import router as routerUser
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



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

schema_view = get_schema_view(
   openapi.Info(
      title="Power Rangers API",
      default_version='v1.0',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)



urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include(router.urls)),   
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
 
    #path("", include("Temporadas.urls")),
    #path("", include("Actor.urls")),
    #path("", include("Capitulos.urls"))
]
