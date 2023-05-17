from .base import *
import os
from dotenv import load_dotenv

load_dotenv(Path.joinpath(BASE_DIR, '.env'))

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