#!usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Administrator'

from django.shortcuts import render_to_response


def error(request):
    return render_to_response('base/error.html')
