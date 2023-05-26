#!/bin/bash

#String de las apps
apps="Actor Capitulos Temporadas User"
#String para el comando para hacer las migraciones
command="manage.py makemigrations $apps"
#Configuracion para el entorno de desarrollo
config="--settings=api.settings.development"

#Elimino los directorios de migrations en las apps
echo "Eliminando migraciones anteriores ..."
. del_migrate.sh
sleep 2

#Creo las migraciones para crear la base de datos
echo "Realizo makemigrations ..."
python3 $command $config
sleep 2

#Creamos las tablas
echo "Realizo migrate ..."
python3 manage.py migrate $config
sleep 2

#Inicio el servidor
echo "Inicio el servidor ..."
python3 manage.py runserver $config

echo "El backend esta listo"

exec "$@"
