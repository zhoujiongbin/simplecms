# -*- coding: utf-8 -*-

# __author__ = 'feng'

from django.shortcuts import render_to_response
from admin.article.models import Article
from admin.user.permission import require_login

# 后台首页显示信息
@require_login
def index(request):
    article_count = Article.objects.count()  # 获取数据库中的文章数目
    return render_to_response('admin/index.html', {'article_count': article_count})
