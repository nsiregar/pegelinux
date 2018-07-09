# Pull base image
FROM python:3.6-alpine

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile /code/Pipfile
RUN apk update && \
 apk add postgresql-libs bash && \
 apk add --virtual .build-deps gcc musl-dev postgresql-dev libffi-dev && \
 pipenv install --deploy --system --skip-lock --dev && \
 apk --purge del .build-deps

# Copy project
COPY . /code/