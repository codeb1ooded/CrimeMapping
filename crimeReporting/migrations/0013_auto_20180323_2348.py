# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-23 18:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('crimeReporting', '0012_auto_20180323_2346'),
    ]

    operations = [
        migrations.CreateModel(
            name='INFORMATION_FILING_APP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('aadharcard', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('crimetype', models.CharField(max_length=100)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('location', models.CharField(max_length=100)),
                ('crime_description', models.CharField(max_length=100)),
                ('date_crime', models.DateField()),
                ('time_crime', models.TimeField()),
                ('complaint_time', models.TimeField()),
                ('complaint_date', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='crime_timeline',
            name='TIME_OF_UPDATE',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 3, 23, 18, 18, 24, 600113, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='fir_report',
            name='COMPLAINT_DATE',
            field=models.DateField(default=datetime.datetime(2018, 3, 23, 18, 18, 24, 598113, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='fir_report',
            name='COMPLAINT_TIME',
            field=models.TimeField(default=datetime.datetime(2018, 3, 23, 18, 18, 24, 598113, tzinfo=utc)),
        ),
    ]