# -*- coding: utf-8 -*-

# __author__ = 'feng'

from django.conf.urls import include, url

from admin.article import views

urlpatterns = [
    url(r'^$', views.article, name='article'),
]