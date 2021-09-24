#!/bin/sh

celery worker --loglevel=info --app={{cookiecutter.code_name}} -Q {{cookiecutter.code_name}}
