# pull official base image
FROM python:3.9.6-alpine


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY . /sensor
RUN pip install -r requirements.txt
