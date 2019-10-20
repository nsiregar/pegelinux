### Compile js
from node:alpine as jsbuilder

WORKDIR /js
RUN mkdir -p /app/assets/js

# Copy js code and dependencies
COPY ./js /js

# install dependecies
RUN yarn install

# build js
RUN yarn build-production

### actual image
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

# copy application js
COPY --from=jsbuilder /app/assets/js/application.js /code/app/assets/js/application.js