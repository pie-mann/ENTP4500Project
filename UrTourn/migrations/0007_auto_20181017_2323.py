# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-17 23:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UrTourn', '0006_auto_20181017_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(upload_to='profile_image'),
        ),
    ]
