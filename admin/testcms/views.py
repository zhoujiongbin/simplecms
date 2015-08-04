from django.shortcuts import render
from django.http import Http404, HttpResponse

def test(request):
    return HttpResponse('Test')
