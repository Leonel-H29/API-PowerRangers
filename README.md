# Documentación de la API REST Power Rangers

<div class="technologies">

[![Docker](https://img.shields.io/badge/Docker-24.0.2-2496ED?style=for-the-badge&logo=Docker)](https://docs.docker.com/get-started/overview/)
[![NGINX](https://img.shields.io/badge/nginx-1.21-009639?style=for-the-badge&logo=NGINX)](https://docs.nginx.com/)
[![Python](https://img.shields.io/badge/Python-3.10.4-3776AB?style=for-the-badge&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2.1-092E20?style=for-the-badge&logo=Django)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.14.0-BA0C2F?style=for-the-badge&logo=Django)](https://www.django-rest-framework.org/)
[![Gunicorn](https://img.shields.io/badge/gunicorn-20.1.0-499848?style=for-the-badge&logo=Gunicorn)](https://gunicorn.org/)
[![PostgreSQL](https://img.shields.io/badge/Postgres-12.15-4169E1?style=for-the-badge&logo=Postgresql)](https://www.postgresql.org/)

</div>

<div>

## Índice

<nav class="menu-docs">

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
  - [Comandos para realizar tareas con Django Rest Framework en Docker](#comandos-para-realizar-tareas-con-django-rest-framework-en-docker)
  - [Acceder a un contenedor por terminal](#acceder-a-un-contenedor-por-terminal)

- [Datos para consumir](#datos-para-consumir)
  - [Actores](#actores)
  - [Temporadas](#temporadas)
  - [Capitulos](#capitulos)
  - [Personajes](#personajes)
  - [Apariciones](#apariciones)

</nav>

</div>

`<!-- ======================================================================= -->`

<div class="introduccion">

# INTRODUCCIÓN

Este documento proporciona la informacion necesaria para explicar en que consiste el proyecto, su arquitectura y ademas proporciona instrucciones detalladas para clonar el proyecto, levantarlo localmente con Docker o con las herramientas necesarias, acceder al navegador y realizar consultas a la API REST.

</div>

<div class="que-es">

# ¿Qué es API REST POWER RANGERS?

El proyecto de la API REST de Power Rangers es una herramienta Open Source creada en Django Rest Framework que contiene una gran cantidad de información relacionada con la popular serie de televisión. El objetivo principal de este proyecto es permitir que cualquier persona interesada pueda consumir esta información y utilizarla para desarrollar su propio proyecto relacionado con Power Rangers.

Esta API REST de Power Rangers está diseñada para ser fácilmente consumible por cualquier persona que tenga un conocimiento básico de programación, lo que la hace ideal para programadores principiantes o desarrolladores experimentados por igual. Además, la API está diseñada para ser altamente escalable, lo que significa que puede ser utilizada en proyectos de cualquier tamaño, desde pequeñas aplicaciones hasta grandes proyectos.

Esta API incluye las siguientes caracteristicas:

- ✅ Paginación
- ✅ Autenticación con JWT
- ✅ Filtros por campos
- ✅ 100 solicitudes por dia para un usuario `no autenticado` y 500 solicitudes por dia para un usuario `autenticado` (Versión de prueba)

Para administracion:

- ✅ Auditoria (Quien consume la API, Operaciones realizadas, etc)
- ✅ Crear usuarios y grupos de usuarios, y asignación de permisos
- ✅ Backups para la base de datos

</div>

<div class="arquitectura">

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

</div>

<div class="clonacion">

## Clonación del proyecto

Clonar un repositorio es una forma común de obtener una copia local de un proyecto alojado en un sistema de control de versiones, como Git. A continuación, se explican las diferentes formas de clonar un repositorio en función de las opciones disponibles:

### 1. Clonar con HTTPS:

Puedes clonar un repositorio utilizando la URL HTTPS proporcionada por el servicio de alojamiento. Utiliza el siguiente comando de Git:

```bash
git clone https://github.com/Leonel-H29/API-PowerRangers.git
```

### 2. Clonar con SSH:

Si has configurado una clave SSH y la has agregado a tu cuenta del servicio de alojamiento, puedes clonar utilizando la URL SSH. Utiliza el siguiente comando de Git:

```bash
git clone git@github.com:Leonel-H29/API-PowerRangers.git
```

### 3. Clonar con GitHub CLI:

Si has instalado la CLI de GitHub (GitHub CLI) en tu sistema, puedes utilizar su comando `gh repo clone` para clonar un repositorio de GitHub. Ejecuta el siguiente comando:

```bash
gh repo clone Leonel-H29/API-PowerRangers
```

### 4. Clonar desde otro servicio de alojamiento:

Si el repositorio está alojado en un servicio de alojamiento diferente a GitHub, como GitLab o Bitbucket, deberás utilizar la URL y los comandos específicos proporcionados por ese servicio.

### 5. Clonar en una ubicación específica:

Por defecto, Git clonará el repositorio en un directorio con el mismo nombre que el repositorio. Si deseas clonar en una ubicación específica, puedes agregar el nombre del directorio como último argumento en el comando. Por ejemplo:

```bash
git clone https://github.com/Leonel-H29/API-PowerRangers.git directorio-destino
```

Estas son algunas de las formas más comunes de clonar un repositorio, dependiendo del servicio de alojamiento y las preferencias de autenticación. Elige el método que mejor se adapte a tu caso y comienza a trabajar con el repositorio en tu entorno local.

</div>

<div class="levantar-proyecto">

# Levantar el proyecto localmente con Docker

1.  Asegúrate de tener Docker instalado en tu máquina, y tener los permisos necesarios.
2.  Abre una terminal y navega hasta el directorio del proyecto clonado.

```bash
cd API-PowerRangers/
```

3.  Ejecuta el siguiente comando para levantar el proyecto utilizando el archivo `docker-compose.yml`:

```bash
docker-compose -f "docker-compose.yml" up -d --build
```

Esto iniciará los contenedores de Docker necesarios para ejecutar la API REST de Django, el administrador de base de datos pgAdmin y la base de datos de Postgres.

En caso no tener 'docker-compose' en tu maquina puedes instalarlo con el siguiente comando:

```bash
sudo apt-get install docker-compose
```

### Ver los contenedores en Docker

1.  Para ver los contenedores en ejecución, utiliza el siguiente comando:

```bash
docker ps
```

Ejemplo de resultado:

```bash

| CONTAINER ID | IMAGE                | COMMAND                | CREATED    | STATUS           | PORTS                                          | NAMES            |
| ------------ | -------------------- | ---------------------- | ---------- | ---------------- | ---------------------------------------------- | ---------------- |
|a3e9301472d1  | nginx:1.0            | "/docker-entrypoint.…" | 7 days ago | Up About an hour |  0.0.0.0:1337->80/tcp, :::1337->80/tcp         |    nginx         |
| 5c91c9331ea1 | backend:1.0          | "sh docker-entrypoin…" | 7 days ago | Up About an hour | 0.0.0.0:8000->8000/tcp, :::8000->8000/tcp      | apirest_djangorf |
| 501f88c036cd | dpage/pgadmin4       | "/entrypoint.sh"       | 7 days ago | Up About an hour | 443/tcp, 0.0.0.0:5050->80/tcp, :::5050->80/tcp | pg_admin         |
| 41ce77e6f37d | postgres:13.3-alpine | "docker-entrypoint.s…" | 7 days ago | Up About an hour | 0.0.0.0:5430->5432/tcp, :::5430->5432/tcp      | db_postgres      |

```

2.  En caso de que quiera ver los logs de cada contenedor utiliza el siguiente comando:

```bash
docker logs -f [CONTAINER ID] | [NAME]
```

3.  Valla a su navegador, e ingrese la siguiente direccion:

        http://localhost:8000/ | http://[DIRECCION_IP]:8000/

Esto te llevará a la página de inicio de la API REST.

![Captura de pantalla de 2023-06-24 22-52-10](https://github.com/Leonel-H29/API-PowerRangers/assets/48606307/ae7ec504-013d-4f25-a1ff-e95e35709929)

### Acceder a la base de PostgreSQL en Docker

Para acceder a tu base de datos en Docker, necesitarás ejecutar un comando para conectarte al contenedor de la base de datos. En tu caso, parece que estás utilizando un contenedor PostgreSQL.

Puedes utilizar el siguiente comando para acceder al contenedor de PostgreSQL:

```bash
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

> _*ACLARACION*:_
>
> - Todas las variables mencionadas deben estar definidas dentro del archivo de entorno correspondiente.
> - Estos pasos tambien son validos en el caso de que tengas instalado PgAdmin 4 instalado localmente en tu computadora sin necesidad de Docker.

</div>

<div>

# Swagger

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

# Datos a tener en cuenta

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

> Recuerda que los valores reales para estas variables pueden variar según la configuración específica de tu proyecto y entorno. Asegúrate de establecer los valores correctos para cada variable de entorno según tus necesidades.

### Comandos para reiniciar, detener y eliminar contenedores en Docker

A continuación se presentan los comandos para reiniciar, detener y eliminar los contenedores en Docker:

- **Para reiniciar los contenedores que se ejecutan en segundo plano:**

```bash
docker-compose -f "docker-compose.yml" restart
```

- **Para detener los contenedores en ejecución:**

```bash
docker-compose -f "docker-compose.yml" stop [CONTAINER ID] | [NAME]
```

- **Para iniciar la ejecucion de los contenedores:**

```bash
docker-compose -f "docker-compose.yml" start [CONTAINER ID] | [NAME]
```

- **Para eliminar los contenedores detenidos y todos los recursos relacionados, como volúmenes y redes:**

```bash
docker-compose -f "docker-compose.yml" down
```

> Recuerda utilizar estos comandos según sea necesario, dependiendo de tus requerimientos y del estado actual de los contenedores en Docker.

### Comandos para realizar tareas con Django Rest Framework en Docker

Aquí tienes una lista de comandos comunes que puedes utilizar para realizar tareas habituales en un entorno de desarrollo Django dentro del contenedor de Docker llamado 'apirest_djangorf':

1. **Crear y configurar un proyecto Django:**

```bash
docker exec -it apirest_djangorf python api/manage.py startproject nombre_proyecto
```

2. **Crear una nueva aplicación Django:**

```bash
docker exec -it apirest_djangorf python api/manage.py startapp nombre_aplicacion
```

3. **Ejecutar migraciones de la base de datos:**

```bash
docker exec -it apirest_djangorf python api/manage.py migrate
```

4. **Crear un superusuario de Django:**

```bash
docker exec -it apirest_djangorf python api/manage.py createsuperuser
```

5. **Iniciar el servidor de desarrollo de Django:**

```bash
docker exec -it apirest_djangorf python api/manage.py runserver 0.0.0.0:8000
```

6. **Ejecutar pruebas de unidad en Django:**

```bash
docker exec -it apirest_djangorf python api/manage.py test
```

7. **Generar documentación de la API con Swagger:**

```bash
docker exec -it apirest_djangorf python api/manage.py generateswagger
```

8. **Recopilar archivos estáticos de Django:**

```bash
docker exec -it apirest_djangorf python api/manage.py collectstatic
```

> Estos son solo algunos ejemplos de comandos que puedes utilizar en un proyecto Django dentro del contenedor de Docker 'apirest_djangorf'. Asegúrate de adaptar los nombres de los proyectos y las aplicaciones a tus necesidades específicas, y ten en cuenta que estos comandos pueden requerir ajustes adicionales dependiendo de la configuración de tu proyecto y entorno.

### Acceder a un contenedor por terminal

Si deseas acceder a un contenedor especifico por medio de la terminal, puedes utilizar el siguiente comando de Docker:

```bash
docker exec -it [CONTAINER ID] | [NAME] bash
```

Este comando ejecuta un nuevo proceso dentro del contenedor y te proporciona un shell interactivo para interactuar directamente con el entorno del contenedor. Dentro del shell, puedes ejecutar comandos y realizar tareas dentro del contenedor de manera similar a como lo harías en una terminal local.

Una vez que hayas ejecutado el comando anterior, se te colocará dentro del contenedor y podrás trabajar con los archivos, ejecutar comandos u otras acciones necesarias dentro del contexto del contenedor.

</div>

<div class='data'>

# Datos para consumir

<div class='data-actores'>

### Actores

`/api/actores/`

#### Descripción:

Esta vista contiene información sobre los actores que han interpretado roles
en las diferentes temporadas de `Power Rangers`. Los actores son quienes dan vida a los personajes
icónicos de la serie.

#### Datos:

| COLUMNA          | TIPO              | DESCRIPCION                                                 |
| ---------------- | ----------------- | ----------------------------------------------------------- |
| id_actor         | integer           | ID unico del actor                                          |
| nombre_actor     | string            | Nombre real del actor                                       |
| nombre_artistico | string            | Nombre artistico del actor                                  |
| foto             | string            | URL de la foto del actor                                    |
| biografia        | string            | URL de la biografia del actor                               |
| personajes       | list (personaje)  | Lista de los personajes que interpreta el actor en la serie |
| updated          | string (datetime) | Fecha de actualizacion del registro                         |

> ##### Ejemplo:
>
> Lista de todos los actores

`Request:`

```json
[GET] http://$URL/api/actores/
```

`Response:`

```json
HTTP 200 OK
{
    "count": 194,
    "next": "http://localhost/api/actores/?limit=100&offset=100",
    "previous": null,
    "results": [
        {
            "id_actor": 1,
            "nombre_actor": "Adam Gardiner",
            "nombre_artistico": "Adam Gardiner",
            "foto": "https://static.wikia.nocookie.net/powerrangers/images/a/a2/Adam_Gardiner.jpg",
            "biografia": "https://en.wikipedia.org/wiki/Adam_Gardiner",
            "personajes": [
                {
                    "id_personaje": 106,
                    "nombre_personaje": "Kamdor",
                    "foto": "https://static.wikia.nocookie.net/powerrangers/images/f/fd/End_of_Kamdor.jpg",
                    "actor": 1,
                    "updated": "2023-09-21T16:27:31.268960Z"
                }
            ],
            "updated": "2023-09-21T16:27:27.595586Z"
        },
        {
            "id_actor": 2,
            "nombre_actor": "Adam Tuominen",
            "nombre_artistico": "Adam Tuominen",
            "foto": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Adam_Tuominem_%286328045377%29.jpg",
            "biografia": "https://es.wikipedia.org/wiki/Adam_Tuominen",
            "personajes": [
                {
                    "id_personaje": 91,
                    "nombre_personaje": "Hunter Bradley",
                    "foto": "https://i.pinimg.com/564x/15/c4/9c/15c49c563e846a96bd2aa674ac1f5f9f.jpg",
                    "actor": 2,
                    "updated": "2023-09-21T16:27:31.268951Z"
                }
            ],
            "updated": "2023-09-21T16:27:27.595588Z"
        },
        ...
    ]
}
```

#### Filtros:

| COLUMNA          | TIPO   |
| ---------------- | ------ |
| nombre_actor     | string |
| nombre_artistico | string |

> ##### Ejemplo
>
> Filtro por `nombre_artistico`

`Request:`

```json
[GET] http://$URL/api/actores/?nombre_artistico=Rick+Medina
```

`Response:`

```json
HTTP 200 OK
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id_actor": 162,
            "nombre_actor": "Ricardo Medina, Jr.",
            "nombre_artistico": "Rick Medina",
            "foto": "https://www.tvguide.com/a/img/hub/2016/01/15/841e73c7-b371-44dc-9ccf-f29881092a2e/150115-news-ricardo-medina-jr.jpg",
            "biografia": "https://es.wikipedia.org/wiki/Ricardo_Medina,_Jr.",
            "personajes": [
                {
                    "id_personaje": 40,
                    "nombre_personaje": "Cole Evans",
                    "foto": "https://i.pinimg.com/originals/66/c7/06/66c706bb2780006eea1e70b63fee703b.jpg",
                    "actor": 162,
                    "updated": "2023-09-21T16:27:31.268920Z"
                },
                {
                    "id_personaje": 56,
                    "nombre_personaje": "Deker",
                    "foto": "https://static.wikia.nocookie.net/powerrangers/images/f/f7/SS_Deker_profile.png",
                    "actor": 162,
                    "updated": "2023-09-21T16:27:31.268930Z"
                }
            ],
            "updated": "2023-09-21T16:27:27.595941Z"
        }
    ]
}
```

> ##### Ejemplo
>
> Filtro por `nombre_actor`

`Request:`

```json
[GET] http://$URL/api/actores/?nombre_actor=Jason+Geiger
```

`Response:`

```json
HTTP 200 OK
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id_actor": 85,
            "nombre_actor": "Jason Geiger",
            "nombre_artistico": "Austin St. John",
            "foto": "https://upload.wikimedia.org/wikipedia/commons/4/41/Austin_St._John_Photo_Op_GalaxyCon_Richmond_2019.jpg",
            "biografia": "https://es.wikipedia.org/wiki/Austin_St._John",
            "personajes": [
                {
                    "id_personaje": 96,
                    "nombre_personaje": "Jason Lee Scott",
                    "foto": "https://static.wikia.nocookie.net/powerrangersserie/images/2/23/01._Gold_Ranger.png/revision/latest?cb=20181023211231&path-prefix=es",
                    "actor": 85,
                    "updated": "2023-09-21T16:27:31.268954Z"
                }
            ],
            "updated": "2023-09-21T16:27:27.595646Z"
        }
    ]
}
```

</div>

<div class='data-temporadas'>

### Temporadas

`/api/temporadas/`

#### Descripción:

Esta vista proporciona información sobre todas las temporadas de `Power Rangers` disponibles.
Cada temporada representa un conjunto de episodios que conforman una historia específica dentro de la
franquicia `Power Rangers`.

#### Datos:

| COLUMNA          | TIPO              | DESCRIPCION                                      |
| ---------------- | ----------------- | ------------------------------------------------ |
| id_temporada     | integer           | ID unico de la temporada                         |
| numero_temporada | integer           | Numero de temporada                              |
| nombre           | string            | Titulo asignado a la temporada                   |
| descripcion      | string            | Descripcion de lo que sucede en la temporada     |
| anio_estreno     | integer           | Año de estreno de la temporada                   |
| foto             | string            | URL relacionada a la temporada                   |
| cancion          | string            | Cancion oficial de la temporada                  |
| basada_en        | string            | Serie, Libro, etc en la que se basa la temporada |
| tematica         | string            | Tematica que abarca la temporada                 |
| capitulos        | list (capitulo)   | Lista de los capitulos emitidos en la temporada  |
| updated          | string (datetime) | Fecha de actualizacion del registro              |

> ##### Ejemplo:
>
> Lista de todas las temporadas

`Request:`

```json
[GET] http://$URL/api/temporadas/
```

`Response:`

```json
HTTP 200 OK
{
    "count": 30,
    "next": null,
    "previous": null,
    "results": [
        {
            "id_temporada": 1,
            "numero_temporada": 1,
            "nombre": "Mighty Morphin Power Rangers (Temporada 1)",
            "descripcion": "Dos astronautas liberan por accidente a una bruja alienígena llamada Rita Repulsa de su prision espacial, en la cual llevaba atrapada 10.000 años. Inmediatamente, Rita y sus secuaces establecen un castillo en la luna e inician un ataque contra la Tierra, con la intención de conquistarla. Zordon, un poderoso hechicero atrapado por Rita en un agujero en el tiempo y su asistente robótico Alpha 5, reclutan a \"un equipo de adolescentes con actitud\" para que se conviertan en los Power Rangers y defiendan la Tierra. Estos primeros Power Rangers, a los que más tarde se incorporará un sexto miembro, son unos amigos compañeros de clase en el instituto de la ciudad de Angel Grove, con sus nuevos poderes y la ayuda de los Dinozords, se enfrentarán a Rita, sus patrulleros de masilla y sus hordas de monstruos, tarea que deberán seguir compaginando con su vida cotidiana de estudiantes adolescentes sin que nadie descubra el secreto.",
            "anio_estreno": 1993,
            "foto": "https://images.justwatch.com/poster/8619651/s592/temporada-1.webp",
            "cancion": "\"Go Go Power Rangers\" por Ron Wasserman",
            "basada_en": "Kyōryū Sentai Zyuranger",
            "tematica": "Dinosaurios",
            "capitulos": [
                {
                    "id_capitulo": 1,
                    "numero_cap": 1,
                    "titulo": "El Inicio",
                    "descripcion": "",
                    "temporada": 1,
                    "updated": "2023-09-21T16:27:29.986931Z"
                },
                {
                    "id_capitulo": 2,
                    "numero_cap": 2,
                    "titulo": "Para Superar el miedo",
                    "descripcion": "",
                    "temporada": 1,
                    "updated": "2023-09-21T16:27:29.986932Z"
                },
                ...
                {
                    "id_capitulo": 60,
                    "numero_cap": 60,
                    "titulo": "Regalo de Cumpleaños",
                    "descripcion": "",
                    "temporada": 1,
                    "updated": "2023-09-21T16:27:29.986967Z"
                }
            ],
            "updated": "2023-09-21T16:27:28.659808Z"
        },
        {
            "id_temporada": 2,
            "numero_temporada": 2,
            "nombre": "Mighty Morphin Power Rangers (Temporada 2)",
            "descripcion": "Tras los incontables fracasos de Rita, el jefe de esta, Lord Zedd, regresa desde sus dominios en el espacio para encargarse de la conquista de la Tierra en persona, destituyendo a Rita y enviándola al exilio como castigo por sus fracasos. Para enfrentarse a Lord Zedd y sus nuevos monstruos y patrulleros de masilla Z, Zordon entrega a los Power Rangers unos nuevos Zords más fuertes, los Thunderzords. La batalla escalará cuando Rita regrese de su exilio y gracias a una poción de amor se case con Lord Zedd, convirtiéndose ambos en una amenaza mucho más peligrosa.",
            "anio_estreno": 1994,
            "foto": "https://images.justwatch.com/poster/8619781/s592/temporada-2.webp",
            "cancion": "\"Go Go Power Rangers\" por Ron Wasserman",
            "basada_en": "Gosei Sentai Dairanger",
            "tematica": "Animales mitológicos",
            "capitulos": [
                {
                    "id_capitulo": 61,
                    "numero_cap": 1,
                    "titulo": "El Motin",
                    "descripcion": "",
                    "temporada": 2,
                    "updated": "2023-09-21T16:27:29.986968Z"
                },
                {
                    "id_capitulo": 62,
                    "numero_cap": 2,
                    "titulo": "El Motin Segunda Parte",
                    "descripcion": "",
                    "temporada": 2,
                    "updated": "2023-09-21T16:27:29.986969Z"
                },
                ...
                {
                    "id_capitulo": 112,
                    "numero_cap": 52,
                    "titulo": "Un malvado Ranger Azul",
                    "descripcion": "",
                    "temporada": 2,
                    "updated": "2023-09-21T16:27:29.986999Z"
                }
            ],
            "updated": "2023-09-21T16:27:28.659809Z"
        },
    ]
}
```

#### Filtros:

| COLUMNA          | TIPO    |
| ---------------- | ------- |
| numero_temporada | integer |
| nombre           | string  |
| anio_estreno     | integer |

> ##### Ejemplo:
>
> Filtro por `numero_temporada`

`Request:`

```json
[GET] http://$URL/api/temporadas/?numero_temporada=10
```

`Response:`

```json
HTTP 200 OK
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id_temporada": 10,
      "numero_temporada": 10,
      "nombre": "Power Rangers Wild Force",
      "descripcion": "Cole Evans es un muchacho que ha vivido con una tribu en la jungla durante muchos años, y que encuentra por casualidad el Animarium, un lugar místico en el que conoce a otros cuatro jóvenes de distintas procedencias que se unen a él para proteger a la Tierra del ataque de una raza de criaturas llamadas Orgs, liderados por el Amo Org, que pretenden contaminar la Tierra. Para enfrentarse a ellos, la princesa Shayla del Animarium les entrega el poder de los Wild Force Rangers, además de servirles de mentora en la batalla que se avecina.",
      "anio_estreno": 2002,
      "foto": "https://images.justwatch.com/poster/8619879/s592/temporada-10.webp",
      "cancion": "\"Power Rangers Wild Force\" por Power Rangers",
      "basada_en": "Hyakujuu Sentai Gaoranger",
      "tematica": "Animales salvajes y orgs",
      "capitulos": [
        {
          "id_capitulo": 419,
          "numero_cap": 1,
          "titulo": "Corazón de León",
          "descripcion": "",
          "temporada": 10,
          "updated": "2023-09-21T16:27:29.987190Z"
        },
        {
          "id_capitulo": 420,
          "numero_cap": 2,
          "titulo": "El despertar del mal",
          "descripcion": "",
          "temporada": 10,
          "updated": "2023-09-21T16:27:29.987190Z"
        },
       ...
        {
          "id_capitulo": 458,
          "numero_cap": 40,
          "titulo": "El final de los Power Rangers (2ª parte)",
          "descripcion": "",
          "temporada": 10,
          "updated": "2023-09-21T16:27:29.987215Z"
        }
      ],
      "updated": "2023-09-21T16:27:28.659815Z"
    }
  ]
}
```

> ##### Ejemplo:
>
> Filtro por `nombre`

`Request:`

```json
[GET] http://$URL/api/temporadas/?nombre=Power%20Rangers%20S.P.D.
```

`Response:`

```json
HTTP 200 OK
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id_temporada": 13,
      "numero_temporada": 13,
      "nombre": "Power Rangers S.P.D.",
      "descripcion": "Es el año 2025. La humanidad ya convive de forma pacífica con formas alienígenas de todo el universo. Sin embargo, el maligno Imperio Troobian decide conquistar la Tierra. Cuando la primera línea de defensa, el A-Squad de la S.P.D., desaparece sin dejar rastro, la protección de la Tierra queda a cargo del B-Squad de la S.P.D., liderados por el alienígena cánido Anubis \"Doggie\" Cruger, que establece en ellos a los Power Rangers S.P.D. Cuando dos antiguos ladrones reformados se unen al equipo como el Red y la Yellow S.P.D. Rangers, las tensiones amenazan con romper al grupo, pero con la amenaza alienígena cerciéndose sobre la Tierra, deben dejar a un lado sus diferencias y entrar en batalla lo más unidos que puedan.",
      "anio_estreno": 2005,
      "foto": "https://images.justwatch.com/poster/54059766/s592/temporada-13.webp",
      "cancion": "\"Power Rangers S.P.D.\" por Bruce Lynch y John Adair",
      "basada_en": "Tokusou Sentai Dekaranger (Tokusatsu)",
      "tematica": "Policías, vehículos y el futuro",
      "capitulos": [
        {
          "id_capitulo": 535,
          "numero_cap": 1,
          "titulo": "El comienzo (1ª parte)",
          "descripcion": "",
          "temporada": 13,
          "updated": "2023-09-21T16:27:29.987260Z"
        },
        {
          "id_capitulo": 536,
          "numero_cap": 2,
          "titulo": "El comienzo (2ª parte)",
          "descripcion": "",
          "temporada": 13,
          "updated": "2023-09-21T16:27:29.987260Z"
        },
        ...
        {
          "id_capitulo": 572,
          "numero_cap": 38,
          "titulo": "Insomnio",
          "descripcion": "",
          "temporada": 13,
          "updated": "2023-09-21T16:27:29.987294Z"
        }
      ],
      "updated": "2023-09-21T16:27:28.659816Z"
    }
  ]
}
```

> ##### Ejemplo:
>
> Filtro por `anio_estreno`

`Request:`

```json
[GET] http://$URL/api/temporadas/?anio_estreno=1998
```

`Response:`

```json
HTTP 200 OK
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id_temporada": 6,
      "numero_temporada": 6,
      "nombre": "Power Rangers In Space",
      "descripcion": "La historia comienza exactamente en el mismo punto en que concluyó Power Rangers: Turbo. Los Rangers adultos, al saber que el planeta de Zordon, Eldar, estaba bajo ataque, decidieron marchar al espacio en un cohete de la NASADA, dejando a Justin atrás con su padre. Acaban llegando a una nave espacial que les atrae, y donde conocen a un Red Ranger llamado Andros, un alienígena del planeta KO-35, que al principio no se fía de ellos. Sin embargo, sabe que necesitará ayuda para rescatar a Zordon...",
      "anio_estreno": 1998,
      "foto": "https://images.justwatch.com/poster/8619798/s592/temporada-6.webp",
      "cancion": "\"Power Rangers In Space\" por Power Rangers",
      "basada_en": "Denji Sentai Megaranger",
      "tematica": "Espacio, tecnología y alienígenas",
      "capitulos": [
        {
          "id_capitulo": 251,
          "numero_cap": 1,
          "titulo": "De la nada (1ª parte)",
          "descripcion": "",
          "temporada": 6,
          "updated": "2023-09-21T16:27:29.987079Z"
        },
        {
          "id_capitulo": 252,
          "numero_cap": 2,
          "titulo": "De la nada (2ª parte)",
          "descripcion": "",
          "temporada": 6,
          "updated": "2023-09-21T16:27:29.987080Z"
        },
        ...
        {
          "id_capitulo": 293,
          "numero_cap": 43,
          "titulo": "Cuenta atrás hacia la destrucción (2ª parte)",
          "descripcion": "",
          "temporada": 6,
          "updated": "2023-09-21T16:27:29.987104Z"
        }
      ],
      "updated": "2023-09-21T16:27:28.659812Z"
    }
  ]
}
```

</div>

<div class='data-capitulos'>

### Capitulos

`/api/capitulos/`

#### Descripción:

Esta vista contiene información sobre los episodios individuales que componen cada temporada de `Power Rangers`.
Cada episodio, también conocido como capítulo, presenta una parte de la trama y la historia general de la temporada.

#### Datos:

| COLUMNA     | TIPO              | DESCRIPCION                                       |
| ----------- | ----------------- | ------------------------------------------------- |
| id_capitulo | integer           | ID unico del capitulo                             |
| numero_cap  | integer           | Numero del capitulo                               |
| titulo      | string            | Titulo del capitulo                               |
| descripcion | string            | Descripcion de lo que sucede en el capitulo       |
| temporada   | integer           | ID de la temporada a la que pertenece el capitulo |
| updated     | string (datetime) | Fecha de actualizacion del registro               |

> ##### Ejemplo:
>
> Lista de todos los capitulos

`Request:`

```json
[GET] http://$URL/api/capitulos/
```

`Response:`

```json
HTTP 200 OK
{
  "count": 969,
  "next": "http://localhost/api/capitulos/?limit=100&offset=100",
  "previous": null,
  "results": [
    {
      "id_capitulo": 1,
      "numero_cap": 1,
      "titulo": "El Inicio",
      "descripcion": "",
      "temporada": 1,
      "updated": "2023-09-21T16:27:29.986931Z"
    },
    {
      "id_capitulo": 2,
      "numero_cap": 2,
      "titulo": "Para Superar el miedo",
      "descripcion": "",
      "temporada": 1,
      "updated": "2023-09-21T16:27:29.986932Z"
    },
    ...
    {
      "id_capitulo": 100,
      "numero_cap": 40,
      "titulo": "Un Viaje al Pasado Segunda Parte",
      "descripcion": "",
      "temporada": 2,
      "updated": "2023-09-21T16:27:29.986991Z"
    }
  ]
}
```

#### Filtros:

| COLUMNA    | TIPO    |
| ---------- | ------- |
| numero_cap | integer |
| titulo     | string  |
| temporada  | integer |

> ##### Ejemplo
>
> Filtro por `numero_cap`

`Request:`

```json
[GET] http://$URL/api/capitulos/?numero_cap=5
```

`Response:`

```json
HTTP 200 OK
{
  "count": 29,
  "next": null,
  "previous": null,
  "results": [
    {
      "id_capitulo": 5,
      "numero_cap": 5,
      "titulo": "Una Música Diferente",
      "descripcion": "",
      "temporada": 1,
      "updated": "2023-09-21T16:27:29.986934Z"
    },
    {
      "id_capitulo": 65,
      "numero_cap": 5,
      "titulo": "Una Imagen equivocada",
      "descripcion": "",
      "temporada": 2,
      "updated": "2023-09-21T16:27:29.986970Z"
    },
    ...
    {
      "id_capitulo": 946,
      "numero_cap": 5,
      "titulo": "Episodio 5",
      "descripcion": "",
      "temporada": 29,
      "updated": "2023-09-21T16:27:29.987514Z"
    }
  ]
}
```

> ##### Ejemplo
>
> Filtro por `titulo`

`Request:`

```json
[GET] http://$URL/api/capitulos/?titulo=Un%20Pez%20muy%20Peligroso
```

`Response:`

```json
HTTP 200 OK
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id_capitulo": 516,
      "numero_cap": 20,
      "titulo": "Un Pez muy Peligroso",
      "descripcion": "",
      "temporada": 12,
      "updated": "2023-09-21T16:27:29.987248Z"
    }
  ]
}
```

> ##### Ejemplo
>
> Filtro por `temporada`

`Request:`

```json
[GET] http://$URL/api/capitulos/?temporada=1
```

`Response:`

```json
HTTP 200 OK
{
  "count": 60,
  "next": null,
  "previous": null,
  "results": [
    {
      "id_capitulo": 1,
      "numero_cap": 1,
      "titulo": "El Inicio",
      "descripcion": "",
      "temporada": 1,
      "updated": "2023-09-21T16:27:29.986931Z"
    },
    {
      "id_capitulo": 2,
      "numero_cap": 2,
      "titulo": "Para Superar el miedo",
      "descripcion": "",
      "temporada": 1,
      "updated": "2023-09-21T16:27:29.986932Z"
    },
    ...
    {
      "id_capitulo": 60,
      "numero_cap": 60,
      "titulo": "Regalo de Cumpleaños",
      "descripcion": "",
      "temporada": 1,
      "updated": "2023-09-21T16:27:29.986967Z"
    }
  ]
}
```

</div>

<div class='data-personajes'>

### Personajes

`/api/personajes/`

#### Descripción:

En esta vista, encontrarás información sobre los personajes icónicos de `Power Rangers`. Cada personaje representa
un héroe, villano u otro individuo importante que forma parte de la historia de la serie.

#### Datos:

| COLUMNA          | TIPO              | DESCRIPCION                              |
| ---------------- | ----------------- | ---------------------------------------- |
| id_personaje     | integer           | ID unico del personaje                   |
| nombre_personaje | string            | Nombre real del personaje                |
| foto             | string            | URL de la foto del personaje             |
| actor            | integer           | Id del actor que interpreta al personaje |
| updated          | string (datetime) | Fecha de actualizacion del registro      |

> ##### Ejemplo
>
> Lista de personajes

`Request:`

```json
[GET] http://$URL/api/personajes/
```

`Response:`

```json
HTTP 200 OK
{
  "count": 215,
  "next": "http://localhost/api/personajes/?limit=100&offset=100",
  "previous": null,
  "results": [
    {
      "id_personaje": 1,
      "nombre_personaje": "Adam Park",
      "foto": "https://static.wikia.nocookie.net/power-rangers-fanon-wiki-2/images/3/37/Green_Turbo_Ranger.png",
      "actor": 102,
      "updated": "2023-09-21T16:27:31.268897Z"
    },
    {
      "id_personaje": 2,
      "nombre_personaje": "Albert Collins",
      "foto": "https://static.wikia.nocookie.net/powerrangers/images/5/52/MrCollinsTF.jpg",
      "actor": 60,
      "updated": "2023-09-21T16:27:31.268898Z"
    },
    ...
    {
      "id_personaje": 99,
      "nombre_personaje": "Jenji",
      "foto": "https://i.pinimg.com/564x/21/df/29/21df299dd6102e5b28c9a72c0a6b8d55.jpg",
      "actor": 146,
      "updated": "2023-09-21T16:27:31.268956Z"
    }
  ]
}
```

#### Filtros:

| COLUMNA          | TIPO    |
| ---------------- | ------- |
| nombre_personaje | string  |
| actor            | integer |

> ##### Ejemplo
>
> Filtro por `nombre_personaje`

`Request:`

```json
[GET] http://$URL/api/personajes/?nombre_personaje=Jenji
```

`Response:`

```json
HTTP 200 OK
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id_personaje": 99,
      "nombre_personaje": "Jenji",
      "foto": "https://i.pinimg.com/564x/21/df/29/21df299dd6102e5b28c9a72c0a6b8d55.jpg",
      "actor": 146,
      "updated": "2023-09-21T16:27:31.268956Z"
    }
  ]
}
```

> ##### Ejemplo
>
> Filtro por `actor`

`Request:`

```json
[GET] http://$URL/api/personajes/?actor=20
```

`Response:`

```json
HTTP 200 OK
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id_personaje": 105,
      "nombre_personaje": "Kai Chen",
      "foto": "https://i.pinimg.com/564x/bd/b0/02/bdb002ed07bc33569bc61aa74cdab594.jpg",
      "actor": 20,
      "updated": "2023-09-21T16:27:31.268959Z"
    }
  ]
}
```

</div>

<div class='data-apariciones'>

### Apariciones

`/api/aparecen/`

#### Descripción:

Esta vista muestra la relación entre los personajes y las temporadas en las que aparecen en la serie `Power Rangers`.
Es una relación N:N que vincula los personajes específicos con las temporadas en las que han participado.

#### Datos:

| COLUMNA      | TIPO             | DESCRIPCION                                            |
| ------------ | ---------------- | ------------------------------------------------------ |
| id_aparicion | integer          | ID unico de la aparicion del personaje en la temporada |
| personaje    | dict(personaje)  | Objeto personaje                                       |
| temporada    | dict (temporada) | Objeto temporada                                       |
| rol          | string           | El rol que ocupa el personaje en la temporada          |
| descripcion  | string           | Descripcion del rol del personaje en esta temporada    |

#### Ejemplo

`Request:`

```json
[GET] http://$URL/api/aparecen/
```

`Response:`

```json
HTTP 200 OK
{
  "count": 251,
  "next": "http://localhost/api/aparecen/?limit=3&offset=3",
  "previous": null,
  "results": [
    {
      "id_aparicion": 1,
      "personaje": {
        "id_personaje": 5,
        "nombre_personaje": "Alpha 5",
        "foto": "https://static.wikia.nocookie.net/powerrangersserie/images/7/79/Alpha_5.jpg",
        "actor": 165,
        "updated": "2023-09-21T16:27:31.268900Z"
      },
      "temporada": {
        "id_temporada": 1,
        "numero_temporada": 1,
        "nombre": "Mighty Morphin Power Rangers (Temporada 1)",
        "descripcion": "Dos astronautas liberan por accidente a una bruja alienígena llamada Rita Repulsa de su prision espacial, en la cual llevaba atrapada 10.000 años. Inmediatamente, Rita y sus secuaces establecen un castillo en la luna e inician un ataque contra la Tierra, con la intención de conquistarla. Zordon, un poderoso hechicero atrapado por Rita en un agujero en el tiempo y su asistente robótico Alpha 5, reclutan a \"un equipo de adolescentes con actitud\" para que se conviertan en los Power Rangers y defiendan la Tierra. Estos primeros Power Rangers, a los que más tarde se incorporará un sexto miembro, son unos amigos compañeros de clase en el instituto de la ciudad de Angel Grove, con sus nuevos poderes y la ayuda de los Dinozords, se enfrentarán a Rita, sus patrulleros de masilla y sus hordas de monstruos, tarea que deberán seguir compaginando con su vida cotidiana de estudiantes adolescentes sin que nadie descubra el secreto.",
        "anio_estreno": 1993,
        "foto": "https://images.justwatch.com/poster/8619651/s592/temporada-1.webp",
        "cancion": "\"Go Go Power Rangers\" por Ron Wasserman",
        "basada_en": "Kyōryū Sentai Zyuranger",
        "tematica": "Dinosaurios",
        "capitulos": [
          {
            "id_capitulo": 1,
            "numero_cap": 1,
            "titulo": "El Inicio",
            "descripcion": "",
            "temporada": 1,
            "updated": "2023-09-21T16:27:29.986931Z"
          },
          ...
          {
            "id_capitulo": 60,
            "numero_cap": 60,
            "titulo": "Regalo de Cumpleaños",
            "descripcion": "",
            "temporada": 1,
            "updated": "2023-09-21T16:27:29.986967Z"
          }
        ],
        "updated": "2023-09-21T16:27:28.659808Z"
      },
      "rol": "Aliados",
      "descripcion": "Definido como \"autómata multifuncional ultra-sensible\", es el robot asistente de Zordon. Se encarga de ser sus manos y pies, operando los controles del Centro de Mando y llamando a los Rangers en caso de emergencia. Alpha 5 quiere a Zordon como un padre y vela por su seguridad en la medida de sus posibilidades. Siempre tiene la preocupación clavada en su personalidad, ya sea por sí mismo o por la seguridad de los que quiere, como Zordon o los Power Rangers, y siempre está pronunciando el gritito de \"¡Ay-ay-ay-ay-ay!\" cuando algo le causa temor, que viene a ser casi siempre. Gracias a la seguridad del Centro de Mando, no tiene nada que temer, pero fuera de él es muy vulnerable a cualquier tipo de ataque, bastando con introducir un disco en la ranura situada en su espalda para reprogramarle por completo para hacer el mal o infectarle con un destructivo virus informático que le ponga en peligro."
    },
    {
      "id_aparicion": 2,
      "personaje": {
        "id_personaje": 20,
        "nombre_personaje": "Billy Cranston",
        "foto": "https://i.ytimg.com/vi/zAaAtpvDafQ/hqdefault.jpg",
        "actor": 48,
        "updated": "2023-09-21T16:27:31.268909Z"
      },
      "temporada": {
        "id_temporada": 1,
        "numero_temporada": 1,
        "nombre": "Mighty Morphin Power Rangers (Temporada 1)",
        "descripcion": "Dos astronautas liberan por accidente a una bruja alienígena llamada Rita Repulsa de su prision espacial, en la cual llevaba atrapada 10.000 años. Inmediatamente, Rita y sus secuaces establecen un castillo en la luna e inician un ataque contra la Tierra, con la intención de conquistarla. Zordon, un poderoso hechicero atrapado por Rita en un agujero en el tiempo y su asistente robótico Alpha 5, reclutan a \"un equipo de adolescentes con actitud\" para que se conviertan en los Power Rangers y defiendan la Tierra. Estos primeros Power Rangers, a los que más tarde se incorporará un sexto miembro, son unos amigos compañeros de clase en el instituto de la ciudad de Angel Grove, con sus nuevos poderes y la ayuda de los Dinozords, se enfrentarán a Rita, sus patrulleros de masilla y sus hordas de monstruos, tarea que deberán seguir compaginando con su vida cotidiana de estudiantes adolescentes sin que nadie descubra el secreto.",
        "anio_estreno": 1993,
        "foto": "https://images.justwatch.com/poster/8619651/s592/temporada-1.webp",
        "cancion": "\"Go Go Power Rangers\" por Ron Wasserman",
        "basada_en": "Kyōryū Sentai Zyuranger",
        "tematica": "Dinosaurios",
        "capitulos": [
          {
            "id_capitulo": 1,
            "numero_cap": 1,
            "titulo": "El Inicio",
            "descripcion": "",
            "temporada": 1,
            "updated": "2023-09-21T16:27:29.986931Z"
          },
          ...
          {
            "id_capitulo": 60,
            "numero_cap": 60,
            "titulo": "Regalo de Cumpleaños",
            "descripcion": "",
            "temporada": 1,
            "updated": "2023-09-21T16:27:29.986967Z"
          }
        ],
        "updated": "2023-09-21T16:27:28.659808Z"
      },
      "rol": "Mighty Morphin Blue Ranger",
      "descripcion": "Es el nerd de la clase, con una inteligencia inversamente proporcional a sus habilidades sociales y a su seguridad en sí mismo. Suele al principio emplear una jerga excesivamente técnica incluso en su vida cotidiana, una jerga que solo Trini puede comprender, soliendo ejercer de intérprete. Al principio, también, carece de habilidades de lucha y le cuesta mucho defenderse sin transformarse, hasta que se apunta a las clases de artes marciales de Jason para mejorar en este aspecto. Con el tiempo y la experiencia, irá aumentando su fuerza y su seguridad en sí mismo, y comenzará a abandonar la jerga técnica según va madurando como luchador y como persona. Por su inteligencia, también es capaz de desarrollar en su laboratorio personal todo tipo de artefactos y herramientas para ayudar al equipo en la pelea, y es capaz de operar en el centro de mando con la misma pericia que el propio Alpha 5. Como Blue Ranger, adquirió los poderes del Triceratops Dinozord en batalla, y su arma personal es la Power Lance. Más adelante recibiría el poder del Unicorn Thunderzord, y después el Wolf Ninjazord y el Blue Shōgunzord."
    },
    {
      "id_aparicion": 3,
      "personaje": {
        "id_personaje": 75,
        "nombre_personaje": "Eugene \"Skull\" Skullovitch",
        "foto": "https://assets.mycast.io/characters/eugene-skullovitch-589038-normal.jpg",
        "actor": 83,
        "updated": "2023-09-21T16:27:31.268941Z"
      },
      "temporada": {
        "id_temporada": 1,
        "numero_temporada": 1,
        "nombre": "Mighty Morphin Power Rangers (Temporada 1)",
        "descripcion": "Dos astronautas liberan por accidente a una bruja alienígena llamada Rita Repulsa de su prision espacial, en la cual llevaba atrapada 10.000 años. Inmediatamente, Rita y sus secuaces establecen un castillo en la luna e inician un ataque contra la Tierra, con la intención de conquistarla. Zordon, un poderoso hechicero atrapado por Rita en un agujero en el tiempo y su asistente robótico Alpha 5, reclutan a \"un equipo de adolescentes con actitud\" para que se conviertan en los Power Rangers y defiendan la Tierra. Estos primeros Power Rangers, a los que más tarde se incorporará un sexto miembro, son unos amigos compañeros de clase en el instituto de la ciudad de Angel Grove, con sus nuevos poderes y la ayuda de los Dinozords, se enfrentarán a Rita, sus patrulleros de masilla y sus hordas de monstruos, tarea que deberán seguir compaginando con su vida cotidiana de estudiantes adolescentes sin que nadie descubra el secreto.",
        "anio_estreno": 1993,
        "foto": "https://images.justwatch.com/poster/8619651/s592/temporada-1.webp",
        "cancion": "\"Go Go Power Rangers\" por Ron Wasserman",
        "basada_en": "Kyōryū Sentai Zyuranger",
        "tematica": "Dinosaurios",
        "capitulos": [
          {
            "id_capitulo": 1,
            "numero_cap": 1,
            "titulo": "El Inicio",
            "descripcion": "",
            "temporada": 1,
            "updated": "2023-09-21T16:27:29.986931Z"
          },
          ...
          {
            "id_capitulo": 60,
            "numero_cap": 60,
            "titulo": "Regalo de Cumpleaños",
            "descripcion": "",
            "temporada": 1,
            "updated": "2023-09-21T16:27:29.986967Z"
          }
        ],
        "updated": "2023-09-21T16:27:28.659808Z"
      },
      "rol": "Aliados",
      "descripcion": "Un maton del instituto donde estudian los Rangers, además de ser compañeros de clase de estos. Tienen una habilidad innata para ponerse a sí mismos en evidencia, ya sea intentando meterse con los Rangers o intentando superarles en cualquier habilidad, acabando casi siempre por los suelos o cubiertos de todo tipo de comida que suelen arrojar sobre sí mismos, o bien son castigados cuando cometen alguna fechoría en el instituto. Cuando los Rangers les salvan a la llegada de Lord Zedd, se proponen hacerse famosos descubriendo sus identidades, pero todos los planes que idean resultan un fracaso. Tras abandonar esta idea, se alistan en la Policía Juvenil de Angel Grove, en principio con la sola idea de llevar uniformes para gustar a las chicas. Según va pasando el tiempo, van evolucionando y madurando, y aunque nunca pierden del todo su personalidad torpe y atolondrada, sí que van abandonando la actitud malévola del principio, y en más de una ocasión, incluso ayudan a los Power Rangers con o sin conocimiento de ello. Desde que se unen a la policía juvenil, se convierten en subordinados del teniente Stone, a quien siempre llevan por la calle de la amargura por su incompetencia en las misiones que les asigna."
    }
    ...
  ]
}
```

</div>

</div>
