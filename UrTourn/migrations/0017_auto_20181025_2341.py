# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-25 23:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UrTourn', '0016_auto_20181025_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='host',
            field=models.CharField(max_length=40),
        ),
    ]
