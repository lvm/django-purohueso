#!/bin/sh
celery beat --loglevel=info --app={{cookiecutter.code_name}}
