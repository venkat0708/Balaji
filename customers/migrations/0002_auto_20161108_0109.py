# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-11-07 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='business_name',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
