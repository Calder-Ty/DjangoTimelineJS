# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-29 05:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0007_auto_20161229_0530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timelineevent',
            name='background',
        ),
    ]
