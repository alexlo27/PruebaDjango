# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-16 20:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convocado', '0005_auto_20160614_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]
