# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-09 14:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20170609_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='users',
            field=models.ManyToManyField(to='account.UserProfile'),
        ),
    ]
