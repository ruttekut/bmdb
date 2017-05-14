# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=250)
    birthtown = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=2000)
    year = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    img_url = models.CharField(max_length=3000)
    stars = models.IntegerField()

    def __str__(self):
        return self.title
