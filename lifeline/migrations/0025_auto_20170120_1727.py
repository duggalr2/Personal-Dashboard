# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-20 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lifeline', '0024_auto_20170119_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_list',
            name='author',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='event_list',
            name='event_url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='side_projects',
            name='resources',
            field=models.CharField(blank=True, default='Url', max_length=500),
        ),
    ]