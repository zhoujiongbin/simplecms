from django.shortcuts import render

from django.http import Http404, HttpResponse

def article(request):
    return HttpResponse('article')