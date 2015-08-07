# -*- coding: utf-8 -*-

from django.shortcuts import render,render_to_response
from admin.cat.models import Cat
from django.http import Http404, HttpResponse,HttpResponseRedirect
from admin.cat.form import AddCat,EditCat
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from admin.user.permission import require_login
from common import function
from django.core.paginator import PageNotAnInteger, Paginator, InvalidPage, EmptyPage

# 分类管理界面
@require_login
def cat(request):
    cat_list = function.get_cats()
    return render_to_response('admin/cat/cat.html',{'cat_list': cat_list})

# 添加分类
@csrf_exempt
@require_login
def add(request):
   if request.method == 'POST':
        cat_name = request.POST['cat_name']
        cat_father = request.POST['cat_father']
        Cat.objects.create(cat_name=cat_name, cat_father=cat_father)
        return HttpResponseRedirect(reverse('cat'))
   else:
        new_cat = AddCat()
        cats = function.get_cats()
   return render_to_response('admin/cat/cat_add.html', {'new_cat': new_cat,'cats':cats})

# 修改分类
@require_login
def edit(request, cat_id):
    cat = Cat.objects.get(cat_id=cat_id)
    if request.method == 'POST':
        cat_change = request.POST['cat_name']
        if cat_change:
            cat.cat_name = cat_change
            cat.cat_father = request.POST['cat_father']
            cat.save()
            return HttpResponseRedirect(reverse('cat'))
        else:
           raise ValueError("修改失败")
    else:
        cats = function.get_cats()
        cat_form = cat
    kwvars ={
         'cat_id': cat_id,
         'cat_form':cat_form,
         'cats':cats
     }
    return render_to_response('admin/cat/cat_editor.html',kwvars,context_instance=RequestContext(request))


# 删除分类
@require_login
def delete(request,cat_id):
    Cat.objects.get(pk=cat_id).delete()
    return HttpResponseRedirect(reverse('cat'))


#关键字搜索分类
def search_by_page(request):
    each_page=2
    if 'q' in request.GET and request.GET['q']:
          q = request.GET['q']
    cat_list=function.get_cat_search(q)
    paginator = Paginator(cat_list,each_page)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        contacts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        contacts = paginator.page(paginator.num_pages)
    return render_to_response('admin/cat/cat.html',{'cat_list': contacts,'q':q,'paginator':paginator})







