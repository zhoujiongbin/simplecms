# -*- coding: utf-8 -*-

from django.shortcuts import render,render_to_response
from admin.cat.models import Cat
from django.http import Http404, HttpResponse,HttpResponseRedirect
from admin.cat.form import AddCat,EditCat
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt

# 分类管理界面
def cat(request):
    cat_list = Cat.objects.all()
    return render_to_response('admin/cat/cat.html',{'cat_list':cat_list})

# 添加分类
@csrf_exempt
def add(request):
   if request.method == 'POST':
       new_cat = AddCat(request.POST)
       if new_cat.is_valid():
           cat_name = new_cat.cleaned_data['cat_name']
           Cat.objects.create(cat_name=cat_name, cat_father=0)
           return HttpResponseRedirect(reverse('cat'))
   else:
        new_cat = AddCat()
   return render_to_response('admin/cat/cat_add.html', {'new_cat': new_cat})

# 修改分类
def edit(request, cat_id):
    cat = Cat.objects.get(cat_id=cat_id)
    if request.method=='POST':
        cat_change = request.POST['cat_name']
        if cat_change:
            cat.cat_name = cat_change
            cat.save()
            return HttpResponseRedirect(reverse('cat'))
        else:
           raise ValueError("修改失败")
    else:
        cat_form = cat
    kwvars ={
         'cat_id': cat_id,
         'cat_form':cat_form,
     }
    return render_to_response('admin/cat/cat_editor.html',kwvars)


# 删除分类
def delete(request,ID):
    Cat.objects.get(cat_id=ID).delete()
    return HttpResponseRedirect(reverse('cat'))







