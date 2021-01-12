from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^client/(?P<pk>[0-9]+)$', views.list_client, name='client'),
    #url(r'^client/<str:pk>/$', views.list_client, name='client'),
]
