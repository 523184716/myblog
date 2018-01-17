#!/usr/bin/env python
#coding:utf-8

from django.conf.urls import  url
import  views
urlpatterns = [
    url(r'index/',views.index,name="index"),
    url(r'login/', views.login, name="login"),
    url(r'asset_allocate/', views.assets, name="assets"),
    url(r'report/', views.report, name="report"),
    url(r'add/([0-9]{2})',views.add,name="add"),
    url(r'delete/',views.delete,name="delete"),
    url(r'modify',views.modify,name="modify"),
    url(r'select/',views.select,name="select"),
    url(r'formget/',views.formget,name="formget"),
]