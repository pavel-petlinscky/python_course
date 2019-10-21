# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='PizzaIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PizzaMenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('ingredients', models.ManyToManyField(related_name='ingredients', to='pizza_app.PizzaIngredient')),
            ],
        ),
        migrations.CreateModel(
            name='PizzaOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, max_length=140)),
                ('delivered', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_delivered', models.DateTimeField(default=None, null=True)),
                ('delivery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pizzas', to='pizza_app.Address')),
                ('exclude', models.ManyToManyField(blank=True, to='pizza_app.PizzaIngredient')),
                ('extra', models.ManyToManyField(blank=True, related_name='pizzas_extras', to='pizza_app.PizzaIngredient')),
                ('kind', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pizzas', to='pizza_app.PizzaMenuItem')),
            ],
        ),
        migrations.CreateModel(
            name='PizzaSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('XL', 'Large'), ('MD', 'Medium'), ('SM', 'Small')], max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='pizzaorder',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pizzas', to='pizza_app.PizzaSize'),
        ),
    ]
