# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
# from django.http import HttpResponse

from django.shortcuts import render
from .models import Client

def list_client(request,pk):
    client=Client.objects.get(id=pk)
    commande=client.commande_set.all()
    context={'client':client,'commande':commande}
    return render(request,'client/list_client.html',context)




 