# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-20 02:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convocado', '0010_auto_20160619_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evidencia_convocatoria',
            name='evidencia',
            field=models.ImageField(upload_to='evidencia/'),
        ),
    ]