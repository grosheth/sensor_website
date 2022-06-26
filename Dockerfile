# pull official base image
FROM python:3.9.6-alpine

# set work directory
WORKDIR /usr/src/sensor

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY . .
RUN pip install -r requirements.txt

# copy project
COPY . .