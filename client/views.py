# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
# from django.http import HttpResponse

from django.shortcuts import render

def list_client(request):
    return render(request,'client/list_client.html')
