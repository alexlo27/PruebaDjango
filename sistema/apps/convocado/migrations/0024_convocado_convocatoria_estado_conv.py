# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-03 19:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convocado', '0023_auto_20160703_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='convocado_convocatoria',
            name='estado_conv',
            field=models.CharField(default='0', max_length=1),
            preserve_default=False,
        ),
    ]