# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-18 18:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logs',
            name='c_date',
            field=models.DateTimeField(),
        ),
    ]
