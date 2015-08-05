from django.shortcuts import render

# Create your views here.
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext
from django.shortcuts import render_to_response
from admin.detail.models import  Detail
from django import forms
import os
import time

class UploadFileForm(forms.Form):
    img=forms.FileField()


def index(request):
    D = Detail()
    detail = Detail.objects.get()
    return render_to_response('base.html', context={'detail': detail},context_instance=RequestContext(request))

def save(request):
    if request.POST.get('title'):
        f = UploadFileForm(request.POST, request.FILES)
        title = request.POST['title']
        introduction = request.POST['introduction']
        handle_uploaded_file(request.FILES['file'])
        logo_path  =handle_uploaded_file(f)
        d = Detail(title=title, logo_path=logo_path, introduction=introduction)
        d.save()
        return HttpResponseRedirect('/admin')

def delete(request, id):
    Detail.objects.get(pk=id).delete()

def handle_uploaded_file(f):
    file_name = ""

    try:
        path = "./upload" + time.strftime('/%Y/%m/%d/')
        if not os.path.exists(path):
            os.makedirs(path)
        file_name = path + f.name
        destination = open(file_name, 'wb+')
        for chunk in f.chunks():
            destination.write(chunk)
        destination.close()
    except Exception as e:
        print(e)
    return file_name
