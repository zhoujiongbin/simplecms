# -*- coding: utf-8 -*-

# __author__ = 'feng'
from admin.cat.models import Cat

# 根据ID获取分类名
def get_cat(id):
    query_set = Cat.objects.get(cat_id=id)
    cat_name = query_set.cat_name
    return cat_name
