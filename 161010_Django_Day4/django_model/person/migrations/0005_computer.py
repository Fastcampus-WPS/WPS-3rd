# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-07 05:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0004_auto_20161007_0540'),
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('num', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
            ],
        ),
    ]
