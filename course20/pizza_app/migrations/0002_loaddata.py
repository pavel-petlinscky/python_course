# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
from django.core.management import call_command

from django.db import migrations

FIXTURE = 'initial'
APP_LABEL = 'pizza_app'


def load_fixture(apps, schema_editor):
    """ Call management command to load fixtures. """

    print()
    call_command('loaddata', FIXTURE, app_label=APP_LABEL)


def unload_fixture(apps, schema_editor):
    """ Brutally deleting all entries for this model. """

    classes = ['PizzaSize', 'PizzaIngredient', 'PizzaMenuItem']

    for klass in classes:
        model_class = apps.get_model(APP_LABEL, klass)
        model_class.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        (APP_LABEL, '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_fixture, reverse_code=unload_fixture),
    ]
