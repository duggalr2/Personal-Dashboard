# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-23 03:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lifeline', '0025_auto_20170120_1727'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
            ],
        ),
    ]
