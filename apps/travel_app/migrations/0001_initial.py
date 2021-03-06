# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-19 21:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_reg_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('travel_date_from', models.DateField()),
                ('travel_date_to', models.DateField()),
                ('all_users', models.ManyToManyField(related_name='all_plans', to='login_reg_app.User')),
                ('user_plans', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login_reg_app.User')),
            ],
        ),
    ]
