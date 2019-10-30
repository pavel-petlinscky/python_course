# -*- coding: utf-8 -*-

"""
To run celery:
`celery --app=pizza_project.celery_app:app worker --loglevel=INFO -E -B`

To run celery monitor:
`python manage.py celerycam`
"""

import os

from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'pizza_project.settings')

app = Celery('pizza')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
