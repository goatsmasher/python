# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-16 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_register_datehired'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='datehired',
            field=models.DateTimeField(),
        ),
    ]