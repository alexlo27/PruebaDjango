# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-24 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convocado', '0013_auto_20160623_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evidencia_convocatoria',
            name='puntaje_calculado',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='evidencia_convocatoria',
            name='puntaje_obtenido',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
