from .base import *
import os
from dotenv import load_dotenv

FILE_ENV= '.env'

load_dotenv(Path.joinpath(BASE_DIR, FILE_ENV))

SECRET_KEY = config("SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = ['*']

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

DJANGO_SUPERUSER_EMAIL=config("DJANGO_SUPERUSER_EMAIL")
DJANGO_SUPERUSER_USERNAME=config("DJANGO_SUPERUSER_USERNAME")
DJANGO_SUPERUSER_PASSWORD=config("DJANGO_SUPERUSER_PASSWORD")

DRF_API_LOGGER_DATABASE = False 
DRF_API_LOGGER_SIGNAL =  False 