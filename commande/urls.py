from django.conf.urls import url

from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^commande/', views.list_commande),
    url(r'^ajouter/',views.ajouter_commande,name='ajouter'),
    url(r'^modifier/(?P<pk>[0-9]+)$',views.modifier_commande,name='modifier'),
    url(r'^supprimer/(?P<pk>[0-9]+)$',views.supprimer_commande,name='supprimer'),
]
