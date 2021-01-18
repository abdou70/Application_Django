# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
#from commande.models import Commande
#from client.models import Client

def home(request):
    return render(request,'compte/inscrip.html')

