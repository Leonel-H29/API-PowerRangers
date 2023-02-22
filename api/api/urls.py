from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("Actor.urls")),
    #path("", include("capitulo.urls")),
    path("", include("Temporadas.urls")),
]
