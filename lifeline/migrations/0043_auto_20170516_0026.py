# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-16 04:26
from __future__ import unicode_literals

import datetime
import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lifeline', '0042_auto_20170515_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='screen_shot',
            field=models.ImageField(blank=True, storage=django.core.files.storage.FileSystemStorage(location='/Users/Rahul/Desktop/Main/Side_projects/project_2/static/screenshot'), upload_to=''),
        ),
        migrations.AlterField(
            model_name='ran_event_list',
            name='start_time',
            field=models.TimeField(default=datetime.time(0, 26, 39, 403007)),
        ),
    ]