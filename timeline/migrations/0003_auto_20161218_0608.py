# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-18 06:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0002_auto_20161218_0605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timelineevent',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='timelineevent',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
