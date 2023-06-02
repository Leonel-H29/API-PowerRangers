# Documentación de la API REST Power Rangers

Este README.md proporciona instrucciones detalladas para clonar el proyecto, levantar el proyecto localmente con Docker Compose, acceder al navegador y realizar consultas a la API REST.

## Clonación del proyecto

1. Clona el repositorio utilizando el siguiente comando:

		git clone https://github.com/Leonel-H29/API-PowerRangers.git

## Levantar el proyecto localmente con Docker

1. Asegúrate de tener Docker Compose instalado en tu máquina.
2. Abre una terminal y navega hasta el directorio del proyecto clonado.
3. Ejecuta el siguiente comando para levantar el proyecto utilizando el archivo `docker-compose.yml`:

		docker-compose -f "docker-compose.yml" up -d --build

Esto iniciará los contenedores de Docker necesarios para ejecutar la API REST de Django y la base de datos de Postgres.

## Ver los contenedores en Docker

1. Para ver los contenedores en ejecución, utiliza el siguiente comando:

		docker ps
			
Ejemplo de resultado:

| CONTAINER ID | IMAGE                | COMMAND                   | CREATED     | STATUS            | PORTS                                      | NAMES            |
|--------------|----------------------|---------------------------|-------------|-------------------|--------------------------------------------|------------------|
| 5c91c9331ea1 | backend:1.0          | "sh docker-entrypoin…"    | 7 days ago  | Up About an hour  | 0.0.0.0:8000->8000/tcp, :::8000->8000/tcp | apirest_djangorf |
| 41ce77e6f37d | postgres:13.3-alpine | "docker-entrypoint.s…"    | 7 days ago  | Up About an hour  | 0.0.0.0:5430->5432/tcp, :::5430->5432/tcp | db_postgres      |


2. En caso de que quiera ver los logs de cada contenedor utiliza el siguiente comando:

		docker logs -f [CONTAINER ID] | [NAME]

		
3. Valla a su navegador, e ingrese la siguiente direccion:

		http://localhost:8000/ | http://[DIRECCION_IP]:8000/

Esto te llevará a la página de inicio de la API REST.

