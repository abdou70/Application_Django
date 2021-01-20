# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
# from django.http import HttpResponse

from django.shortcuts import render
from .models import Client
from django.contrib.auth.decorators import login_required
# from commande.filters import CommandeFiltre


@login_required(login_url='access')
def list_client(request,pk):
    client=Client.objects.get(id=pk)
    commande=client.commande_set.all()
    commande_total=commande.count()
    # myFilter=CommandeFiltre
    context={'client':client,'commande':commande,'commande_total':commande_total}
    return render(request,'client/list_client.html',context)




 