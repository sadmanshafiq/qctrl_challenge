# pull official base image
FROM python:3.8.0-alpine

# set work directory
WORKDIR /backend_qctrl

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /backend_qctrl/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /backend_qctrl/