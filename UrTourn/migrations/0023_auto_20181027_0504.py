# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-27 05:04
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('UrTourn', '0022_auto_20181026_1848'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_content', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('reciever', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='tournament',
            name='endTime',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 27, 5, 4, 30, 752877, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournament',
            name='startTime',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 27, 5, 4, 39, 547136, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
