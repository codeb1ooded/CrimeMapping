# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-25 06:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('crimeReporting', '0014_auto_20180324_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crime_timeline',
            name='TIME_OF_UPDATE',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 3, 25, 6, 28, 38, 598540, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='fir_report',
            name='COMPLAINT_DATE',
            field=models.DateField(default=datetime.datetime(2018, 3, 25, 6, 28, 38, 597632, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='fir_report',
            name='COMPLAINT_TIME',
            field=models.TimeField(default=datetime.datetime(2018, 3, 25, 6, 28, 38, 597602, tzinfo=utc)),
        ),
    ]
