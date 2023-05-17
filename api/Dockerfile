# Utiliza la imagen base de Python 3.9
FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED 1

# Configura el directorio de trabajo	
WORKDIR /app


# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instala las dependencias
RUN pip install  --no-cache-dir -r requirements.txt

# Copia el código de la aplicación al contenedor
COPY . .

# Expone el puerto 8081
EXPOSE 8081

# Ejecuta el comando para arrancar el servidor
#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]
ENTRYPOINT [ "/app/docker-entrypoint.sh" ]
