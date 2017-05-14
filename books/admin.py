# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Author, Books
from django.contrib import admin

# Register your models here.
admin.site.register(Author)
admin.site.register(Books)
