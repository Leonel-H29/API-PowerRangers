#!/bin/sh

#String de las apps
apps="Actor Capitulos Temporadas User"
#String para el comando para hacer las migraciones
command="manage.py makemigrations $apps"
#Configuracion para el entorno de produccion
config="--settings=api.settings.production"

#Elimino los directorios de migrations en las apps
echo "Eliminando migraciones anteriores ..."
. del_migrate.sh
sleep 2

#Almaceno los archivos estaticos
echo "Creando los archivos estaticos ..."
python manage.py collectstatic --no-input $config
sleep 2

#Creo las migraciones para crear la base de datos
echo "Realizo makemigrations ..."
python $command $config
sleep 2

#Espero a que la base de datos este lista
python manage.py wait_db $config
sleep 2

#Creamos las tablas
echo "Realizo migrate ..."
python manage.py migrate $config
sleep 2

#Creo y controlo el superusuario del sistema
python manage.py create_admin $config
sleep 2

#Inicio el servidor
echo "Inicio el servidor ..."
python manage.py runserver 0.0.0.0:8000 $config

echo "El backend esta listo"

exec "$@"
