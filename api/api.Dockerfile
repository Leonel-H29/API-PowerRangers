FROM python:3.8-alpine


ENV PYTHONUNBUFFERED=1


WORKDIR /usr/src/backend


COPY requirements.txt .


RUN pip install  --no-cache-dir -r requirements.txt


EXPOSE 8081


# CMD [ "python", "manage.py", "runserver", "0.0.0.0:8081"]
ENTRYPOINT [ "/usr/src/api/docker-entrypoint.sh" ]