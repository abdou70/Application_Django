from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^access/$', views.home,name='access'),
]
