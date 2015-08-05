#coding:utf-8
from django.shortcuts import render,render_to_response
from admin.cat.models import Cat
from django.http import Http404, HttpResponse,HttpResponseRedirect
from admin.cat.form import AddCat,EditCat
from django.core.urlresolvers import reverse

#分类列表
def indexView(request):
    cat_list = Cat.objects.all()
    return render_to_response('admin/cat/indexView.html',{'catlist':cat_list})

#添加分类
def addCat(request):
   if request.method == 'POST':
       newCat = AddCat(request.POST)
       if newCat.is_valid():
           cat_name = newCat.cleaned_data['cat_name']
           Cat.objects.create(cat_name=cat_name,cat_father=1)
           return HttpResponseRedirect(reverse('cat_view'))
   else:
        newCat = AddCat()
   return render_to_response('admin/cat/add.html',{'newCat':newCat})

#修改分类
def editCat(request,ID):
    cat = Cat.objects.get(cat_id=ID)
    if request.method=='POST':
        catChange = request.POST['cat_name']
        if catChange:
            cat.cat_name = catChange
            cat.save()
            return HttpResponseRedirect(reverse('cat_view'))
        else:
           raise ValueError("请输入修改信息")
    else:
        catForm = cat
    kwvars ={
         'ID':ID,
         'catForm':catForm,
     }
    return render_to_response('admin/cat/edit.html',kwvars)


#删除分类
def deleteCat(request,ID):
    Cat.objects.get(cat_id=ID).delete()
    return HttpResponseRedirect(reverse('cat_view'))







