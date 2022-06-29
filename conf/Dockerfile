FROM python:3.9.12-slim-buster
ARG PROJECT_ENVIRONMENT=dev

# Copy python necessities
RUN mkdir /python
COPY conf/python/.pylintrc /python
COPY conf/python/mypy.ini /python

# Update system and install pipenv
RUN apt-get update && apt-get install --no-install-recommends --assume-yes bash
# RUN python -m pip install --upgrade pip
COPY Pipfile Pipfile.lock ./
RUN pip install pipenv && pipenv install --dev --system

# Make workdir
RUN mkdir /app
WORKDIR /app
ADD src/ /app/
