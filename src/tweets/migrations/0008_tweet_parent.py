# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 22:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0007_auto_20171021_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tweets.Tweet'),
        ),
    ]
