# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-07 05:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0003_auto_20161007_0540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='major',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
