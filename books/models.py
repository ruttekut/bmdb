# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=250)
    birthtown = models.CharField(max_length=100)
    age = models.IntegerField(null=True)

    def __str__(self):
        return self.name


# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=2000)
    year = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    stars = models.IntegerField(null=True)
    uitgever = models.CharField(max_length=1000, null=True)
    pagenumbers = models.CharField(max_length=5, null=True)
    img_url = models.CharField(max_length=1000, default='http://www.workyouenjoy.com/wp-content/uploads/2012/07/Red-Book.jpg')

    def __str__(self):
        return self.title
