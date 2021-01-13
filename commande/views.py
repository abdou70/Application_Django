# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
# from django.http import HttpResponse

from django.shortcuts import render,redirect
from .forms import CommandeForm
from .models import Commande

def list_commande(request):
    commandes=Commande.objects.all()
    context={'commandes':commandes}
    return render(request,'commande/commande.html')

def ajouter_commande(request):
    form=CommandeForm()
    if request.method=='POST':
        form=CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}        
    return render(request,'commande/commande.html',context)  

def modifier_commande(request,pk):
    commande=Commande.objects.get(id=pk)
    form=CommandeForm(instance=commande)
    if request.method=='POST':
        form=CommandeForm(request.POST,instance=commande)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}        
    return render(request,'commande/commande.html',context)    
  
