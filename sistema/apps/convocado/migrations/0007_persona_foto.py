# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-17 18:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convocado', '0006_auto_20160616_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='foto',
            field=models.ImageField(default='', upload_to='photo_perfil/'),
            preserve_default=False,
        ),
    ]
