# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-14 19:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20170514_1920'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='hometown',
            new_name='birthtown',
        ),
        migrations.RemoveField(
            model_name='author',
            name='birthyear',
        ),
    ]
