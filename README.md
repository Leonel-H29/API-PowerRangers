# Documentación de la API REST Power Rangers

![alt_text](https://img.shields.io/badge/Docker-24.0.2-2496ED?style=for-the-badge&logo=Docker)
![alt_text](https://img.shields.io/badge/nginx-1.21-009639?style=for-the-badge&logo=NGINX)
![alt_text](https://img.shields.io/badge/Python-3.10.4-3776AB?style=for-the-badge&logo=Python)
![alt_text](https://img.shields.io/badge/Django-4.2.1-092E20?style=for-the-badge&logo=Django)
![alt_text](https://img.shields.io/badge/DRF-3.14.0-BA0C2F?style=for-the-badge&logo=Django)
![alt_text](https://img.shields.io/badge/gunicorn-20.1.0-499848?style=for-the-badge&logo=Gunicorn)
![alt_text](https://img.shields.io/badge/Postgres-12.15-4169E1?style=for-the-badge&logo=Postgresql)

## Índice

- [INTRODUCCIÓN](#introducción)
- [¿Qué es API REST POWER RANGERS?](#qué-es-api-rest-power-rangers)
- [Arquitectura de Software](#arquitectura-de-software)
  - [Cliente](#cliente)
  - [Servidor web: Nginx](#servidor-web-nginx)
  - [Backend: API REST de Django con Gunicorn](#backend-api-rest-de-django-con-gunicorn)
  - [Base de datos: PostgreSQL](#base-de-datos-postgresql)
  - [Contenedores de Docker](#contenedores-de-docker)
  - [Diagrama de la arquitectura](#diagrama-de-la-arquitectura)
- [Clonación del proyecto](#clonación-del-proyecto)
- [Levantar el proyecto localmente con Docker](#levantar-el-proyecto-localmente-con-docker)
  - [Ver los contenedores en Docker](#ver-los-contenedores-en-docker)
  - [Acceder a la base de PostgreSQL en Docker](#acceder-a-la-base-de-postgresql-en-docker)
  - [Configuración de pgAdmin 4 para conectar a la base de datos PostgreSQL en Docker](#configuración-de-pgadmin-4-para-conectar-a-la-base-de-datos-postgresql-en-docker)
- [Swagger](#swagger)
  - [¿Qué es Swagger?](#qué-es-swagger)
  - [Documentación de la API REST de Django con Swagger](#documentación-de-la-api-rest-de-django-con-swagger)
- [Datos a tener en cuenta](#datos-a-tener-en-cuenta)
  - [Archivo de variables de entorno](#archivo-de-variables-de-entorno)
  - [Comandos para reiniciar, detener y eliminar contenedores en Docker](#comandos-para-reiniciar-detener-y-eliminar-contenedores-en-docker)
  - [Variables de entorno](#variables-de-entorno)
    - [Variables de entorno de la base de datos Postgres](#variables-de-entorno-de-la-base-de-datos-postgres)
    - [Variables de entorno de Postgres](#variables-de-entorno-de-postgres)
    - [Variables de entorno de la aplicación Django](#variables-de-entorno-de-la-aplicación-django)
    - [Variables de entorno de la API REST](#variables-de-entorno-de-la-api-rest)
    - [Variables de entorno de archivos y datos](#variables-de-entorno-de-archivos-y-datos)
    - [Variables de entorno para superusuario de Django](#variables-de-entorno-para-superusuario-de-django)
    - [Variables de entorno para PgAdmin](#variables-de-entorno-para-pgadmin)

`/*==================================================================================*/`

# INTRODUCCIÓN

Este documento proporciona la informacion necesaria para explicar en que consiste el proyecto, su arquitectura y ademas proporciona instrucciones detalladas para clonar el proyecto, levantarlo localmente con Docker o con las herramientas necesarias, acceder al navegador y realizar consultas a la API REST.

# ¿Qué es API REST POWER RANGERS?

El proyecto de la API REST de Power Rangers es una herramienta Open Source creada en Django Rest Framework que contiene una gran cantidad de información relacionada con la popular serie de televisión. El objetivo principal de este proyecto es permitir que cualquier persona interesada pueda consumir esta información y utilizarla para desarrollar su propio proyecto relacionado con Power Rangers.

Esta API REST de Power Rangers está diseñada para ser fácilmente consumible por cualquier persona que tenga un conocimiento básico de programación, lo que la hace ideal para programadores principiantes o desarrolladores experimentados por igual. Además, la API está diseñada para ser altamente escalable, lo que significa que puede ser utilizada en proyectos de cualquier tamaño, desde pequeñas aplicaciones hasta grandes proyectos.

# Arquitectura de Software

En este proyecto, se utiliza una arquitectura de software de tipo cliente-servidor basada en contenedores Docker para implementar una aplicación web. A continuación, se describen los componentes principales de la arquitectura y cómo interactúan entre sí:

### Cliente

El cliente en este caso son los navegadores web utilizados por los usuarios para acceder a la aplicación. Los navegadores web realizan solicitudes HTTP al servidor web y muestran la interfaz de usuario al usuario final.

### Servidor web: Nginx

En este proyecto, Nginx actúa como un servidor web y también como un proxy inverso. Un proxy inverso es un tipo de servidor que actúa como intermediario entre los clientes y los servidores de backend. Recibe las solicitudes de los clientes y las redirige a los servidores de backend correspondientes para procesarlas y obtener las respuestas.

Nginx implementa el proxy inverso dirigiendo las solicitudes entrantes a la API REST de Django ejecutada por Gunicorn. Esto significa que Nginx recibe las solicitudes de los clientes y luego las redirige a Gunicorn, que es el servidor de aplicaciones que ejecuta la API REST de Django. Nginx también se encarga de enrutar las respuestas generadas por el backend y devolverlas al cliente.

Esta configuración con un proxy inverso es comúnmente utilizada para mejorar el rendimiento y la seguridad de una aplicación web. Nginx puede manejar eficientemente las solicitudes de los clientes y distribuir la carga de trabajo entre varios servidores de backend, lo que permite escalar la aplicación y proporcionar una mejor experiencia a los usuarios.

### Backend: API REST de Django con Gunicorn

En el backend de este proyecto, se utiliza una API REST de Django para proporcionar funcionalidad y servicios a los clientes. Gunicorn, que significa "Green Unicorn", es un servidor de aplicaciones compatible con WSGI (Web Server Gateway Interface) que se utiliza para ejecutar la API REST de Django.

El funcionamiento de Gunicorn implica varios pasos:

1.  Cuando se inicia Gunicorn, se configura para manejar una cierta cantidad de procesos de trabajadores (workers) y hilos (threads) para atender las solicitudes de los clientes.
2.  Cuando se recibe una solicitud HTTP de un cliente, Gunicorn selecciona un proceso de trabajador disponible para manejarla.
3.  El proceso de trabajador carga la aplicación de la API REST de Django y procesa la solicitud. Esto puede implicar la ejecución de código de la aplicación, acceder a la base de datos, realizar cálculos y generar una respuesta.
4.  Una vez que se genera la respuesta, el proceso de trabajador la envía de vuelta a través de Gunicorn, que a su vez se encarga de enviarla al cliente que realizó la solicitud.
5.  Gunicorn es ampliamente utilizado en proyectos de Django debido a su capacidad para manejar múltiples solicitudes concurrentes de manera eficiente, lo que mejora el rendimiento y la escalabilidad de la aplicación.

La API REST de Django proporciona puntos finales (endpoints) que definen las operaciones disponibles en la aplicación. Estos puntos finales permiten a los clientes realizar solicitudes HTTP (como GET, POST, PUT, DELETE) para interactuar con los datos y funcionalidades proporcionados por el backend.

### Base de datos: PostgreSQL

En este proyecto, se utiliza PostgreSQL como el sistema de gestión de bases de datos. PostgreSQL es un potente sistema de base de datos relacional de código abierto y es ampliamente utilizado en aplicaciones web debido a su capacidad de escalabilidad y características avanzadas.

pgAdmin es una herramienta de administración de bases de datos PostgreSQL que se utiliza para interactuar con el servidor de base de datos y administrar las bases de datos y los objetos relacionados. Proporciona una interfaz gráfica para realizar tareas como crear, modificar y eliminar tablas, consultas SQL, gestionar usuarios y permisos, realizar copias de seguridad y mucho más.

En el contexto de este proyecto, pgAdmin se utiliza como una interfaz de administración conveniente y visual para trabajar con la base de datos PostgreSQL. Permite a los desarrolladores y administradores de bases de datos interactuar con la base de datos de manera eficiente

### Contenedores de Docker

Cada componente de la arquitectura (servidor web Nginx, backend Django con Gunicorn y base de datos PostgreSQL) se ejecuta dentro de contenedores de Docker. Docker permite la encapsulación de cada componente junto con sus dependencias y configuraciones en un entorno aislado y portátil. Esto facilita la implementación consistente de la aplicación en diferentes entornos y simplifica el proceso de desarrollo, implementación y escalamiento.

Los contenedores de Docker se pueden crear utilizando archivos de configuración llamados Dockerfiles y se ejecutan utilizando imágenes de Docker. Cada contenedor se ejecuta como una instancia aislada y ligera que contiene todos los elementos necesarios para que el componente correspondiente funcione correctamente.

### Diagrama de la arquitectura

![Presentación sin título](https://github.com/Leonel-H29/API-PowerRangers/assets/48606307/c5f62b17-c783-4815-9531-a1d32913ae81)

Esta arquitectura de software de tipo cliente-servidor basada en contenedores Docker proporciona una forma eficiente y escalable de implementar y ejecutar la aplicación web, permitiendo la fácil replicación y distribución de los componentes en diferentes entornos de desarrollo y producción.

## Clonación del proyecto

- Clona el repositorio utilizando el siguiente comando:

      git clone https://github.com/Leonel-H29/API-PowerRangers.git

## Levantar el proyecto localmente con Docker

1.  Asegúrate de tener Docker instalado en tu máquina, y tener los permisos necesarios.
2.  Abre una terminal y navega hasta el directorio del proyecto clonado.

        cd API-PowerRangers/

3.  Ejecuta el siguiente comando para levantar el proyecto utilizando el archivo `docker-compose.yml`:

        docker-compose -f "docker-compose.yml" up -d --build

Esto iniciará los contenedores de Docker necesarios para ejecutar la API REST de Django, el administrador de base de datos pgAdmin y la base de datos de Postgres.

En caso no tener 'docker-compose' en tu maquina puedes instalarlo con el siguiente comando:

    	sudo apt-get install docker-compose

### Ver los contenedores en Docker

1.  Para ver los contenedores en ejecución, utiliza el siguiente comando:

        docker ps

Ejemplo de resultado:

```

| CONTAINER ID | IMAGE                | COMMAND                | CREATED    | STATUS           | PORTS                                          | NAMES            |
| ------------ | -------------------- | ---------------------- | ---------- | ---------------- | ---------------------------------------------- | ---------------- |
|a3e9301472d1  | nginx:1.0            | "/docker-entrypoint.…" | 7 days ago | Up About an hour |  0.0.0.0:1337->80/tcp, :::1337->80/tcp         |    nginx         |
| 5c91c9331ea1 | backend:1.0          | "sh docker-entrypoin…" | 7 days ago | Up About an hour | 0.0.0.0:8000->8000/tcp, :::8000->8000/tcp      | apirest_djangorf |
| 501f88c036cd | dpage/pgadmin4       | "/entrypoint.sh"       | 7 days ago | Up About an hour | 443/tcp, 0.0.0.0:5050->80/tcp, :::5050->80/tcp | pg_admin         |
| 41ce77e6f37d | postgres:13.3-alpine | "docker-entrypoint.s…" | 7 days ago | Up About an hour | 0.0.0.0:5430->5432/tcp, :::5430->5432/tcp      | db_postgres      |

```

2.  En caso de que quiera ver los logs de cada contenedor utiliza el siguiente comando:

        docker logs -f [CONTAINER ID] | [NAME]

3.  Valla a su navegador, e ingrese la siguiente direccion:

        http://localhost:8000/ | http://[DIRECCION_IP]:8000/

Esto te llevará a la página de inicio de la API REST.

![Captura de pantalla de 2023-06-24 22-52-10](https://github.com/Leonel-H29/API-PowerRangers/assets/48606307/ae7ec504-013d-4f25-a1ff-e95e35709929)

### Acceder a la base de PostgreSQL en Docker

Para acceder a tu base de datos en Docker, necesitarás ejecutar un comando para conectarte al contenedor de la base de datos. En tu caso, parece que estás utilizando un contenedor PostgreSQL.

Puedes utilizar el siguiente comando para acceder al contenedor de PostgreSQL:

```
docker exec -it [CONTAINER ID] | [NAME]  psql -U <username> -d <database_name>
```

Reemplaza `[CONTAINER ID]` o `[NAME]` con el ID o su nombre del contenedor de PostgreSQL, para `<username>` y `<database_name>` se deben colocar los valores establecidos en `POSTGRES_USER` y `POSTGRES_DB` que se encuentan en el archivo de entorno.
Esto te abrirá una sesión interactiva de PostgreSQL en el contenedor, donde podrás ejecutar consultas SQL y realizar acciones en tu base de datos.

### Configuración de pgAdmin 4 para conectar a la base de datos PostgreSQL en Docker

1. Asegúrate de que el contenedor de PostgreSQL esté en ejecución y funcionando correctamente. Puedes verificarlo utilizando el comando `docker ps` y asegurándote de que el contenedor `db_postgres` esté en estado "Up".

2. Abre un navegador web e ingresa la siguiente URL: `http://localhost:5050` | `http://[DIRECCION_IP]:5050` . Esto te llevará a la interfaz de pgAdmin 4.

![Captura de pantalla de 2023-06-24 22-58-35](https://github.com/Leonel-H29/API-PowerRangers/assets/48606307/11478921-ab9b-4e6f-bee7-f7978efc6876)

3. Si es la primera vez que usas pgAdmin 4, debes ingresar con el usuario y contraseña establecida en `PGADMIN_DEFAULT_USERNAME` y `PGADMIN_DEFAULT_USERNAME`.

4. Una vez que hayas establecido la contraseña maestra, se te dirigirá a la página de inicio de pgAdmin 4. Haz clic en el botón "Add New Server" (Agregar nuevo servidor) en el panel izquierdo o selecciona "Create" (Crear) > "Server" (Servidor) en la barra de menú superior.

![Captura de pantalla de 2023-06-24 23-04-42](https://github.com/Leonel-H29/API-PowerRangers/assets/48606307/c9ebd1be-b0bb-42d2-8fcb-5266bef69259)

6. En la pestaña "General" (General), ingresa un nombre descriptivo para el servidor en el campo "Name" (Nombre), puede ser el que quieras.

![Captura de pantalla de 2023-06-24 22-52-36](https://github.com/Leonel-H29/API-PowerRangers/assets/48606307/692919d5-fe17-4a87-984e-171089438f12)

7. Cambia a la pestaña "Connection" (Conexión). Aquí es donde configurarás los detalles de conexión a la base de datos PostgreSQL en el contenedor Docker.

   - En el campo "Host name/address" (Nombre/dirección del host), ingresa el `<container_name>` que se seria este caso `db_postgres`
   - En el campo "Port" (Puerto), ingresa `5432` para que coincida con el puerto mapeado en el contenedor Docker.
   - En el campo "Maintenance database" (Base de datos de mantenimiento), ingresa el nombre de la base de datos a la que deseas conectarte, el nombre puede encontrarse en la variable `DB_NAME`.
   - En el campo "Username" (Nombre de usuario), ingresa el nombre de usuario de la base de datos, el valor se encuentra en `DB_USER`.
   - En el campo "Password" (Contraseña), ingresa la contraseña correspondiente al usuario de la base de datos, el valor se encuentra en `DB_PASSWORD`.

![Captura de pantalla de 2023-06-24 22-53-00](https://github.com/Leonel-H29/API-PowerRangers/assets/48606307/826aab91-283d-49f3-80eb-16ca34de372f)

8. Haz clic en el botón "Save" (Guardar) para guardar la configuración del servidor.

9. En el panel izquierdo, deberías ver el servidor que acabas de agregar. Haz clic en él para expandirlo y mostrar las bases de datos disponibles.

Ahora has configurado correctamente pgAdmin 4 para conectarse a la base de datos PostgreSQL dentro del contenedor Docker. Puedes explorar las bases de datos, ejecutar consultas SQL y realizar otras operaciones de administración utilizando la interfaz de pgAdmin 4.

_*ACLARACION*:_ Todas las variables mencionadas deben estar definidas dentro del archivo de entorno correspondiente.

## Swagger

### ¿Qué es Swagger?

Swagger es una herramienta que permite describir, diseñar y documentar APIs de forma sencilla y estandarizada. Proporciona una especificación llamada OpenAPI Specification (anteriormente conocida como Swagger Specification) que define el formato de la documentación de la API. Esta especificación describe los endpoints, los parámetros, los esquemas de datos, las respuestas y otra información relevante para utilizar y comprender la API.

La documentación generada con Swagger es altamente legible y visualmente atractiva. Además, Swagger facilita la interacción con la API a través de su interfaz de usuario interactiva, permitiendo probar los endpoints directamente desde el navegador.

### Documentación de la API REST de Django con Swagger

Si estás utilizando Django para construir una API REST y has integrado Swagger en tu proyecto, puedes acceder a la documentación de la API a través de la ruta `/docs` en tu aplicación web.

1. Asegurate tener el contenedor de la API REST de Django levantada.

2. Abre tu navegador web y navega a la siguiente dirección: `http://localhost:8000/docs` (o la URL correspondiente donde se esté ejecutando tu servidor de desarrollo de Django).

3. Verás la interfaz de usuario de Swagger, que muestra la documentación generada automáticamente para tu API REST de Django. Aquí podrás explorar los diferentes endpoints, los parámetros esperados, las respuestas y otros detalles de la API.

4. Puedes probar los endpoints directamente desde la interfaz de Swagger. Simplemente haz clic en un endpoint, proporciona los parámetros requeridos (si los hay) y ejecuta la solicitud para ver la respuesta obtenida.

La documentación generada por Swagger te brinda una visión clara de tu API REST de Django y facilita su comprensión y utilización tanto para ti como para otros desarrolladores que interactúen con ella.

![Captura de pantalla de 2023-04-02 16-07-34](https://github.com/Leonel-H29/API-PowerRangers/assets/48606307/3cff9689-65f0-43cc-93e9-9837905fc240)

## Datos a tener en cuenta

### Archivo de variables de entorno

El proyecto utiliza archivos de variables de entorno para configurar ciertos valores específicos del entorno. Asegúrate de tener los siguientes archivos de variables de entorno:

1. `.env`: Este archivo contiene las variables de entorno para el entorno de desarrollo local. Aquí puedes definir variables como claves de API, credenciales de bases de datos locales, etc.

2. `prod.env`: Este archivo contiene las variables de entorno para el entorno de producción. Debes configurar las variables adecuadas para tu entorno de producción, como las claves de API y las credenciales de bases de datos en producción.

- Si deseas no utilizar un archivo de variables de entorno de desarrollo lo puedes hacer sin problema, no es tan necesario ocultar los valores de esas variables ya que estamos trabajando en un entorno controlado, la unica sugerencia es tratar de evitar de utilizar datos personales reales, personales y que deberian ser privados.
- Asegúrate de mantener el archivo de variables de entorno de produccion de manera segura y no los compartas públicamente, ya que pueden contener información confidencial.

### Variables de entorno

En este proyecto, se utilizan diversas variables de entorno para configurar y personalizar diferentes aspectos del entorno de desarrollo y producción. A continuación, se explican cada una de las variables y para qué se utilizan:

#### Variables de entorno de la base de datos Postgres:

- `DB_NAME`: Nombre de la base de datos utilizada por el proyecto.
- `DB_USER`: Nombre de usuario para acceder a la base de datos.
- `DB_PASSWORD`: Contraseña del usuario de la base de datos.
- `DB_HOST`: Dirección o nombre de host de la base de datos.
- `DB_PORT`: Puerto en el que se ejecuta la base de datos.

#### Variables de entorno de Postgres:

- `POSTGRES_USER`: Nombre de usuario para acceder al servidor de base de datos PostgreSQL.
- `POSTGRES_PASSWORD`: Contraseña para el usuario del servidor de base de datos PostgreSQL.
- `POSTGRES_DB`: Nombre de la base de datos principal de PostgreSQL.

#### Variables de entorno de la aplicación Django:

- `SECRET_KEY`: Clave secreta utilizada por Django para la generación de tokens y la protección de datos sensibles.

#### Variables de entorno de la API REST:

- `API_HOST`: Host o dirección de la API REST.
- `API_PORT`: Puerto en el que se ejecuta la API REST.

#### Variables de entorno de archivos y datos:

- `FILE_DATA`: Nombre del archivo de datos utilizado por la aplicación.

#### Variables de entorno para superusuario de Django:

- `DJANGO_SUPERUSER_EMAIL`: Correo electrónico del superusuario de Django.
- `DJANGO_SUPERUSER_USERNAME`: Nombre de usuario del superusuario de Django.
- `DJANGO_SUPERUSER_PASSWORD`: Contraseña del superusuario de Django.

#### Variables de entorno para PgAdmin:

- `PGADMIN_DEFAULT_EMAIL`: Correo electrónico del usuario administrador de PgAdmin.
- `PGADMIN_DEFAULT_USERNAME`: Nombre de usuario del usuario administrador de PgAdmin.
- `PGADMIN_DEFAULT_PASSWORD`: Contraseña del usuario administrador de PgAdmin.

Recuerda que los valores reales para estas variables pueden variar según la configuración específica de tu proyecto y entorno. Asegúrate de establecer los valores correctos para cada variable de entorno según tus necesidades.

### Comandos para reiniciar, detener y eliminar contenedores en Docker

A continuación se presentan los comandos para reiniciar, detener y eliminar los contenedores en Docker:

- Para reiniciar los contenedores que se ejecutan en segundo plano:

      docker-compose -f "docker-compose.yml" restart

- Para detener los contenedores en ejecución:

      docker-compose -f "docker-compose.yml" stop [CONTAINER ID] | [NAME]

- Para iniciar la ejecucion de los contenedores

      docker-compose -f "docker-compose.yml" stop [CONTAINER ID] | [NAME]

- Para eliminar los contenedores detenidos y todos los recursos relacionados, como volúmenes y redes:

      docker-compose -f "docker-compose.yml" down

Recuerda utilizar estos comandos según sea necesario, dependiendo de tus requerimientos y del estado actual de los contenedores en Docker.
