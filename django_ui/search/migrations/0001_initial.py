# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 18:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('price', models.IntegerField()),
                ('crime', models.IntegerField()),
                ('school', models.IntegerField()),
                ('income', models.IntegerField()),
                ('cta', models.IntegerField()),
            ],
        ),
    ]
