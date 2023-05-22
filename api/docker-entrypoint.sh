#!/bin/bash

#Hago un listado de todos los directorios y los almaceno en una variable
dirs_app=$(ls -d */)
#Delimitador de cadena
delimiter='/'
#Array de directorios que no son apps
no_apps=("api" "apps" "data" "venv" "postgres" "init-scripts")

command="manage.py makemigrations"
config="--settings=api.settings.production"

for x in $dirs_app; do
	#Separo la cadena
	app=$(echo $x | cut -d$delimiter -f1)

	value=0
	
	#Verifico si el nombre de la cadena pertenece al array de no_apps
	for dir in "${no_apps[@]}"; do
		if [ "$app" == "$dir" ]; then
			value=1
			break
		fi
	done

	if [ $value == 0 ]; then
		#Concateno para formar el resto del comando
		command="$command $app"
	fi
done

#Creo las migraciones para crear la base de datos
echo "Realizo makemigrations ..."
python3 $command
sleep 2

#Espero a que la base de datos este lista
python3 manage.py wait_db $config
sleep 2

#Creamos las tablas
echo "Realizo migrate ..."
python manage.py migrate $config
sleep 2

#Inicio el servidor
echo "Inicio el servidor ..."
python3 manage.py runserver 0.0.0.0:$PORT $config

echo "El backend esta listo"

exec "$@"
