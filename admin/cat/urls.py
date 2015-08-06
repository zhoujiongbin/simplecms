# -*- coding: utf-8 -*-

# __author__ = 'feng'
from django.conf.urls import include, url

from admin.cat import views

urlpatterns = [
    url(r'^$', views.cat, name='cat'),
    url(r'^add/$',views.add,name='cat_add'),
    url(r'^edit/(?P<cat_id>\d+)/$', views.edit, name='cat_edit'),
    url(r'^delete/(?P<cat_id>\d+)/$',views.delete,name='cat_delete'),
]