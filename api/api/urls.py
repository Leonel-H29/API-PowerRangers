from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("Actor.urls")),
    path("", include("Capitulos.urls")),
    path("", include("Temporadas.urls")),
]
