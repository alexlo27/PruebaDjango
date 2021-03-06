# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-13 21:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('convocado', '0003_auto_20160526_1427'),
    ]

    operations = [
        migrations.CreateModel(
            name='persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('ap_pat', models.CharField(max_length=30)),
                ('ap_mat', models.CharField(max_length=30)),
                ('dni', models.CharField(max_length=8)),
                ('fecha_nac', models.DateTimeField()),
                ('estado_civil', models.CharField(max_length=1)),
                ('sexo', models.CharField(max_length=1)),
                ('direccion', models.CharField(max_length=50)),
                ('ubigeo', models.CharField(max_length=6)),
                ('direccion_act', models.CharField(max_length=50)),
                ('telefono', models.CharField(blank=True, max_length=10, null=True)),
                ('celular', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('ubigeo_act', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='ubigeo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codDpto', models.CharField(max_length=2)),
                ('codProv', models.CharField(max_length=2)),
                ('codDist', models.CharField(max_length=2)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='convocado',
            name='nombre',
        ),
        migrations.AddField(
            model_name='convocado',
            name='persona',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='convocado.persona'),
            preserve_default=False,
        ),
    ]
