# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-10 23:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UrTourn', '0002_auto_20181010_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='rank',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
