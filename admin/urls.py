# -*- coding: utf-8 -*-

# __author__ = 'feng'
from django.conf.urls import include, url


urlpatterns = [
    url(r'^article/', include('admin.article.urls')),
    url(r'^user/', include('admin.user.urls')),
    url(r'^cat/', include('admin.cat.urls')),
    url(r'^detail/', include('admin.detail.urls')),
    url(r'^test/',include('admin.testcms.urls')),
]
