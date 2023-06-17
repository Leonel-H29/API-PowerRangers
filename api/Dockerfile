# Utiliza la imagen base de Python 3.9
FROM python:3.10.4-alpine3.15

ENV PYTHONUNBUFFERED 1

# Configura el directorio de trabajo
WORKDIR /app

RUN apk update \
	&& apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev \
	&& pip install --no-cache-dir --upgrade pip


# Copia el archivo requirements.txt al contenedor
COPY ./requirements.txt ./

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación al contenedor
COPY ./ ./

# Copia el archivo docker-entrypoint.sh al contenedor
COPY ./scripts-sh/docker-entrypoint.sh ./scripts-sh/docker-entrypoint.sh

# Otorga permisos de ejecución al archivo docker-entrypoint.sh
RUN chmod +x ./scripts-sh/docker-entrypoint.sh

# Ejecuta el comando para arrancar el servidor
CMD ["sh","./scripts-sh/docker-entrypoint.sh"]
