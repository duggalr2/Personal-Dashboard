# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-11 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lifeline', '0013_rough_todo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Side_Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('timeframe', models.CharField(max_length=300)),
            ],
        ),
    ]