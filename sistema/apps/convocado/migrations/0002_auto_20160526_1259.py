# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 17:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evaluacion', '0005_auto_20160520_0956'),
        ('convocado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='convocado_convocatoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntaje', models.IntegerField(blank=True, null=True)),
                ('convocado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='convocado.convocado')),
                ('convocatoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evaluacion.convocatoria')),
            ],
        ),
        migrations.CreateModel(
            name='evidencia_aconvocatoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evidencia', models.CharField(max_length=30)),
                ('numero_evidencia', models.CharField(blank=True, max_length=20, null=True)),
                ('cargo_rol', models.CharField(max_length=60)),
                ('puntaje_obte', models.IntegerField()),
                ('caracteristica_conv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evaluacion.caracteristica_conv')),
                ('convocado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='convocado.convocado_convocatoria')),
            ],
        ),
        migrations.CreateModel(
            name='tipo_evidencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('estado', models.CharField(max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='evidencia_aconvocatoria',
            name='tipo_evidencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='convocado.tipo_evidencia'),
        ),
    ]
