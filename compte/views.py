# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import CreerUtilisateur

# Create your views here.
#from commande.models import Commande
#from client.models import Client

def inscription(request):
    form=CreerUtilisateur(request.POST)
    context={'form':form}
    return render(request,'compte/inscrip.html',context)

def accespage(request):
    context={}
    return render(request,'compte/access.html',context)




