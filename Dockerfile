
FROM python:3.10

ENV DockerHOME=/home/app/webapp

RUN mkdir -p $DockerHOME

WORKDIR $DockerHOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY . $DockerHOME
RUN pip install -r requirements.txt


RUN pip install celery redis


CMD celery -A code_check -l info  