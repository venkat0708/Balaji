# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-11-08 18:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0002_category_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='expense',
            new_name='name',
        ),
    ]
