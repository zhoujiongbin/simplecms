# -*- coding: utf-8 -*-

# __author__ = 'feng'
from django.http import HttpResponse
from django.shortcuts import render_to_response
from admin.article.models import Article

# 后台首页显示信息
def index(request):
    article_count = Article.objects.count()  # 获取数据库中的文章数目
    return render_to_response('admin/index.html', {'article_count': article_count})
