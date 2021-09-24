from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{cookiecutter.code_name}}.settings')

app = Celery('{{cookiecutter.code_name}}')
app.config_from_object('{{cookiecutter.code_name}}.celeryconf', namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
