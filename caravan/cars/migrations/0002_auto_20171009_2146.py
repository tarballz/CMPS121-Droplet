# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-09 21:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Red'), (1, 'Blue'), (2, 'Green'), (3, 'Purple')]),
        ),
    ]