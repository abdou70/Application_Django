from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^inscrip/$', views.inscription,name='inscrip'),
    url(r'^access/$', views.accespage,name='access'),
]
