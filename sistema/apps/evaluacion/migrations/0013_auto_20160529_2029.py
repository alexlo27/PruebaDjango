# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 01:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluacion', '0012_auto_20160529_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caracteristica_conv',
            name='puntaje',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
