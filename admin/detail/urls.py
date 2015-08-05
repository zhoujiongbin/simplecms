# -*- coding: utf-8 -*-

# __author__ = 'feng'

from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.detail, {'template': 'admin/detail/detail.html'}, name='detail'),
    url(r'^edit/', views.detail, {'template': 'admin/detail/detail_editor.html'}, name='detail_edit'),
    url(r'^add/', views.detail, {'template': 'admin/detail/detail_add.html'}, name='detail_add'),
    url(r'^save/', views.save, name='detail_save'),
    url(r'^update/', views.update, name='detail_update'),
]