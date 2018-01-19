#!/usr/bin/env python
#coding:utf-8

from django.conf.urls import  url

from views import  *

urlpatterns = [
    url(r'index/',index,name="index"),
    url(r'login/',login,name="login"),
    url(r'article/(\d+)',article,name="article"),
    url(r'asset_list/',asset,name="asset_list"),
]