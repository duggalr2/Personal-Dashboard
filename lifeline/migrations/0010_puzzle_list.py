# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-03 01:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lifeline', '0009_quote_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='Puzzle_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
    ]
