# pull official base image
FROM python:3.9.6-alpine

# set work directory
WORKDIR /sensor

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./ .
COPY . .
RUN pip install -r requirements.txt
