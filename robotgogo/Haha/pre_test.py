# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
from django.shortcuts import render_to_response
import os
 
# 表单


def run(request):
    return render_to_response('pre-test.html')
 
# 接收请求数据


def search(request):
    request.encoding='utf-8'
    if 'q' in request.GET:
        message = '你搜索的内容为: ' + request.GET['q']
        command = 'echo'+' '+request.GET['q']+'>ddd'
        os.system(command)
    else:
        message = '你提交了空表单'
    return HttpResponse(message)
