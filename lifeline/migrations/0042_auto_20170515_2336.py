# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-16 03:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lifeline', '0041_auto_20170503_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='category',
            field=models.CharField(choices=[('Research', 'Research'), ('Interest', 'Interest'), ('Script', 'Script'), ('School', 'School')], default='Interest', max_length=150),
        ),
        migrations.AlterField(
            model_name='ran_event_list',
            name='start_time',
            field=models.TimeField(default=datetime.time(23, 36, 47, 788226)),
        ),
    ]
