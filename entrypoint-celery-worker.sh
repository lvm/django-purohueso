#!/bin/sh

celery worker --loglevel=info --app=purohueso -Q purohueso
