from django.shortcuts import render

# Create your views here.
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext
from django.shortcuts import render_to_response
from admin.detail.models import Detail
from django import forms
import os
import time
from admin.user.permission import require_login

class UploadFileForm(forms.Form):
    file = forms.FileField()

# 根据url跳转至信息管理界面或者信息编辑界面或者信息添加界面
@require_login
def detail(request, template):
    try:
        d = Detail.objects.get(id=1)   # 获取公司信息
    except Detail.DoesNotExist:
        d = None
    return render_to_response(template, context={'detail': d}, context_instance=RequestContext(request))


# 保存添加的信息
@require_login
def save(request):
    if request.POST.get('title'):
        f = UploadFileForm(request.POST, request.FILES)
        title = request.POST['title']
        introduction = request.POST['introduction']
        logo_path = handle_uploaded_file(request.FILES['file'])

        d = Detail(title=title, logo_path=logo_path, introduction=introduction)
        d.save()
        return HttpResponseRedirect('/admin/detail')

# 更新信息
@require_login
def update(request):
    if request.POST.get('detail_id'):
        detail_id = request.POST.get('detail_id')
        title = request.POST['title']
        introduction = request.POST['introduction']
        d = Detail.objects.filter(id=int(detail_id))
        if request.FILES.get('file'):
            logo_path = handle_uploaded_file(request.FILES['file'])
            d.update(title=title, logo_path=logo_path, introduction=introduction)
        else:
            d.update(title=title, introduction=introduction)
        return HttpResponseRedirect('/admin/detail')

# 删除公司信息
@require_login
def delete(request, id):
    Detail.objects.get(pk=id).delete()

# 处理上传的文件，保存到本地服务器
def handle_uploaded_file(f):
    file_name = ""

    try:
        path = "./static/upload" + time.strftime('/%Y/%m/%d/')
        path_save = 'D:/Documents/code/simplecms/static/upload' + time.strftime('/%Y/%m/%d/')
        if not os.path.exists(path):
            os.makedirs(path)
        file_name = path_save + f.name
        file_name_save = path + f.name
        destination = open(file_name, 'wb+')
        for chunk in f.chunks():
            destination.write(chunk)
        destination.close()
    except Exception as e:
        print(e)
    file_path = file_name_save.lstrip('./static/')
    return file_path
