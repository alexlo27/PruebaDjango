# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-27 22:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convocado', '0017_auto_20160627_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='foto',
            field=models.ImageField(default='', upload_to='foto_perfil/'),
            preserve_default=False,
        ),
    ]
