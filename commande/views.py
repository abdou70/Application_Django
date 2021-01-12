# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
# from django.http import HttpResponse

from django.shortcuts import render

def list_commande(request):
    commandes=Commande.objects.all()
    context={'commandes':commandes}
    return render(request,'commande/commande.html')
