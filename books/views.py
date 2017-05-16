# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
# from forms import UserForm


def index(request):
    return render(request, 'home/home.html')


def register(request):
    return render(request, 'home/register.html')
