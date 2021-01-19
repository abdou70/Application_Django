# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .forms import CreerUtilisateur
from django.contrib import messages

# Create your views here.
#from commande.models import Commande
#from client.models import Client

def inscription(request):
    form=CreerUtilisateur()
    if request.method=='POST':
        form=CreerUtilisateur(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Compte Cree avec success')
            return redirect('access')
    context={'form':form}
    return render(request,'compte/inscrip.html',context)

def accespage(request):
    context={}
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('acceuil')
        else:
            messages.info(request,"Verifier votre nom d'utilisateur ou votre mots de passe")    
    return render(request,'compte/access.html',context)

def logout(request):
    
    return redirect('access')




