# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='posted_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]