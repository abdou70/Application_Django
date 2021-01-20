# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
# from django.http import HttpResponse

from django.shortcuts import render
from commande.models import Commande
from client.models import Client
from django.contrib.auth.decorators import login_required

@login_required(login_url='access')
def home(request):
    commandes=Commande.objects.all()
    clients=Client.objects.all()
    context={'commandes':commandes,'clients':clients}
    return render(request,'produit/acceuil.html',context)
