from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth.views import LogoutView
from Temporadas.urls import router as routerTemp
from Actor.urls import router as routerAct
from Capitulos.urls import router as routerCap
from User.urls import router as routerUser
# from documentation.urls import router as routerDoc
from documentation.views import DocumentationViewSet
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
# router.extend(routerDoc)

schema_view = get_schema_view(
    openapi.Info(
        title="Power Rangers API",
        default_version='v1.0',
        description="API REST Open Source con la temática de la serie de televisión 'Power Rangers' en Español (Latino)",
        terms_of_service="https://github.com/Leonel-H29/API-PowerRangers",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

url = 'api/'
urlpatterns = [
    path(url + 'admin/', admin.site.urls),
    path(url + 'logout/', LogoutView.as_view(), name='logout'),
    path(url, include(router.urls)),
    path(url + 'docs/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    # path(url + 'documentation/', DocumentationViewSet.as_view(), name='documentation')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
