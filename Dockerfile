FROM python:3.8-alpine
LABEL author="mauro@sdf.org"

ARG UID=1000
ARG GID=1000

ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV USER purohueso
ENV HOME /app
WORKDIR $HOME

COPY requirements.txt /app/requirements.txt

RUN apk add --no-cache \
       --virtual build-deps \
       musl-dev postgresql-dev \
       build-base python3-dev zlib-dev git \
    && apk add --no-cache \
       postgresql-libs libpq \
    && pip install -U pip \
    && pip install -r /app/requirements.txt \
    && rm -fr /app/.cache \
    && apk --purge del build-deps \
    && addgroup -S $USER -g $GID \
    && adduser -S -G $USER -u $UID -h $HOME $USER

COPY . /app

EXPOSE 8000
USER $USER
