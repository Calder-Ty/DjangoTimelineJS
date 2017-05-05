# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-18 05:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TimelineEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('display_date', models.CharField(max_length=75)),
                ('headline', models.CharField(max_length=75)),
                ('text', models.TextField()),
                ('media', models.URLField()),
                ('media_credit', models.CharField(max_length=75)),
                ('media_caption', models.CharField(max_length=140)),
                ('media_thumbnail', models.URLField()),
                ('slide_type', models.CharField(max_length=30)),
                ('group', models.CharField(max_length=75)),
                ('background', models.CharField(max_length=200)),
            ],
        ),
    ]
