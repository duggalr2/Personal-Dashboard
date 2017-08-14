# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-28 03:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.crypto


class Migration(migrations.Migration):

    dependencies = [
        ('lifeline', '0032_auto_20170216_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='slug_field',
            field=models.SlugField(default=django.utils.crypto.get_random_string),
        ),
        migrations.AlterField(
            model_name='side_projects',
            name='category',
            field=models.CharField(choices=[('Script_C', 'Script_Current'), ('Script_F', 'Script_Future'), ('SP_current', 'SideProject_Current'), ('SP_future', 'SideProject_Future'), ('Script_I', 'Script_Idea'), ('SP_I', 'SideProject_Idea')], default='Script_C', max_length=60),
        ),
    ]