# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-10 14:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluacion', '0016_caracteristica_conv_sub_caract'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caracteristica_conv',
            name='sub_caract',
        ),
    ]