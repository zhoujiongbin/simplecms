# -*- coding: utf-8 -*-

# __author__ = 'feng'
from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='admin_index'),
    url(r'^article/', include('admin.article.urls')),
    url(r'^user/', include('admin.user.urls')),
    url(r'^cat/', include('admin.cat.urls')),
    url(r'^detail/', include('admin.detail.urls')),
]
