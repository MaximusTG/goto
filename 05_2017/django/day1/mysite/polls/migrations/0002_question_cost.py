# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-14 09:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='cost',
            field=models.IntegerField(default=0),
        ),
    ]
