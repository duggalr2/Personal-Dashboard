# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-19 00:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lifeline', '0035_ran_event_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ran_event_list',
            name='end_time',
        ),
    ]
