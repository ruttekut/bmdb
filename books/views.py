# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Books


# Create your views here.
def index(request):
    allbooks = Books.objects.all()
    return render(request, 'home/home.html', {'allbooks': allbooks})
