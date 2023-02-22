#!/bin/bash

dirs_app=$(ls -d */)
delimiter='/'
for x in $dirs_app; do
	read -a app <<< "$x"
	echo ${app[0]}
	#echo $x
	#python3 manage.py makemigrations $x 
done

#python3 manage.py migrate 
