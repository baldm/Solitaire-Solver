# DOCKERFILE COPIED FROM :
# https://testdriven.io/blog/fastapi-docker-traefik/

# Dockerfile

# pull the official docker image
FROM python:3.9.4-slim

# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install depencies to run opencv
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .