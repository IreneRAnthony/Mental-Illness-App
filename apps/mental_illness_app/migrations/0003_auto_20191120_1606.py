# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-21 00:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mental_illness_app', '0002_auto_20191120_1354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coin',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='coin_amount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Coin',
        ),
    ]
