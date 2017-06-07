# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-06 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_books_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='account',
        ),
        migrations.AddField(
            model_name='books',
            name='genre',
            field=models.CharField(choices=[(b'romance', b'Romance'), (b'science', b'Science'), (b'romans', b'Romans')], max_length=20, null=True),
        ),
    ]