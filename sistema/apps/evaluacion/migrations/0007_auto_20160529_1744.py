# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-29 22:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluacion', '0006_auto_20160529_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caracteristica_conv',
            name='numeracion',
            field=models.IntegerField(),
        ),
    ]
