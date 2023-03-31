#!/bin/bash

#Elimino la base de datos
rm db.sqlite3


##Busco los directorios con el nombre de '__pycache__' y 'migrations'

directorios=$(find . -type d -name "__pycache__" && find . -type d -name "migrations")


#Recorro la lista y elimino cada directorio y el contenido de cada directorio

for x in $directorios; do
	#echo $x
	rm -r $x
done

