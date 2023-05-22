# Utiliza la imagen base de Python 3.9
FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED 1

# Configura el directorio de trabajo
WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        musl-dev \
        postgresql-dev \
        python3-dev \
        libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia el archivo requirements.txt al contenedor
COPY ./requirements.txt ./

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación al contenedor
COPY ./ ./

# Copia el archivo docker-entrypoint.sh al contenedor
COPY docker-entrypoint.sh ./docker-entrypoint.sh

# Otorga permisos de ejecución al archivo docker-entrypoint.sh
RUN chmod +x docker-entrypoint.sh

# Ejecuta el comando para arrancar el servidor
CMD ["./docker-entrypoint.sh"]
