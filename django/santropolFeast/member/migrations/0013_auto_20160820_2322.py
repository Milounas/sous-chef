# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-20 23:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0012_clientscheduledstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientscheduledstatus',
            name='change_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='clientscheduledstatus',
            name='change_state',
            field=models.CharField(choices=[('START', 'Start'), ('END', 'End')], default='START', max_length=5),
        ),
    ]
