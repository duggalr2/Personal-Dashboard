# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-02 02:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lifeline', '0004_goal_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('author', models.CharField(max_length=200)),
            ],
        ),
    ]
