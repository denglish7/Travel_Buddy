# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 01:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='image',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
