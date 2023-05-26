from .base import *
import os
from dotenv import load_dotenv

FILE_ENV= 'prod.env'

load_dotenv(Path.joinpath(BASE_DIR, FILE_ENV))

SECRET_KEY = config("SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = ['*']

#Configuracion de la base de datos Postgres
DB_NAME=config("DB_NAME")
DB_USER=config("DB_USER")
DB_PASSWORD=config("DB_PASSWORD")
DB_HOST=config("DB_HOST")
DB_PORT=config("DB_PORT")

POSTGRES_READY = (
    DB_NAME is not None
    and DB_USER is not None
    and DB_PASSWORD is not None
    and DB_HOST is not None
    and DB_PORT is not None
)

#print(POSTGRES_READY)

if POSTGRES_READY:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": config("DB_NAME"),
            "USER": config("DB_USER"),
            "PASSWORD": config("DB_PASSWORD"),
            "HOST": config("DB_HOST"),
            "DATABASE_PORT": config("DB_PORT"),
        },
}

STATIC_ROOT=Path.joinpath(BASE_DIR, 'static_files')
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

DJANGO_SUPERUSER_EMAIL=config("DJANGO_SUPERUSER_EMAIL")
DJANGO_SUPERUSER_USERNAME=config("DJANGO_SUPERUSER_USERNAME")
DJANGO_SUPERUSER_PASSWORD=config("DJANGO_SUPERUSER_PASSWORD")