# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-19 21:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20161216_0917'),
        ('belt_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='created_by',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to='main_app.Register'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='user',
            field=models.ManyToManyField(related_name='wishes', to='main_app.Register'),
        ),
    ]