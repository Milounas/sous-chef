# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-19 19:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0015_auto_20160518_0317'),
    ]

    operations = [
        migrations.AddField(
            model_name='referencing',
            name='work_information',
            field=models.TextField(blank=True, null=True, verbose_name='Work information'),
        ),
    ]