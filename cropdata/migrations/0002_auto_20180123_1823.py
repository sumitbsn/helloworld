# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-23 18:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cropdata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='entry_time',
            field=models.DateTimeField(blank=True, max_length=50, null=True),
        ),
    ]