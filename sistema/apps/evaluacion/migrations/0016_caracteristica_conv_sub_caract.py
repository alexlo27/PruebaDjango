# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 20:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluacion', '0015_auto_20160530_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='caracteristica_conv',
            name='sub_caract',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]
