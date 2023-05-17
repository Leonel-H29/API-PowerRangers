#!/bin/bash

#Hago un listado de todos los directorios y los almaceno en una variable
dirs_app=$(ls -d */)
#Delimitador de cadena
delimiter='/'

command="manage.py makemigrations"

for x in $dirs_app; do
	#Separo la cadena
	app=$(echo $x | cut -d$delimiter -f1)
	
	#Verifico si el nombre de la cadena no es igual al del directorio principal
	#y al directorio para hacer scraping de datos
	if [ "$app" != "api" ] && [ "$app" != "data" ]; then
		#Concateno para formar el resto del comando
		command="$command $app"
	fi
done

#Creo las migraciones para crear la base de datos
echo "Realizo makemigrations"
python3 $command
sleep 2

#Creamos las tablas
echo "Realizo migrate"
python3 manage.py migrate 
sleep 2

#Inicio el servidor
echo "Inicio el servidor"
python3 manage.py runserver 0.0.0.0:8081

echo "El backend esta listo"

exec "$@"

