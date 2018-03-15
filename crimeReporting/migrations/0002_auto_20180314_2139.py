# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-14 16:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crimeReporting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fir_report',
            name='STATUS_OF_CRIME',
            field=models.CharField(default=b'Pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='fir_report',
            name='LOCATION_LAT',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='fir_report',
            name='LOCATION_LONG',
            field=models.FloatField(),
        ),
    ]