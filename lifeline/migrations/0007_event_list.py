# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-02 17:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lifeline', '0006_course_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('event_url', models.URLField()),
            ],
        ),
    ]