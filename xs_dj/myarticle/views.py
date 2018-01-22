# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,HttpResponse
from models import *
# Create your views here.
from template_form import *
from django import  forms
def index(request):
    obj = Article.objects.all()
    return render(request,'myarticle/index.html',locals())


def login(request):
    return  render(request,'myarticle/login.html',locals())

def article(request,article_id):
    obj = Article.objects.filter(id=article_id)
    return render(request,'myarticle/article_display.html',locals())

def asset(request):
    obj = Asset_List.objects.all()
    return  render(request,'myarticle/asset_list.html',locals())

def add_asset(request):
    if request.method == "POST":
        return HttpResponse("ok")
    else:
        obj = Asset_Form()
        print obj
        return  render(request,'myarticle/add _asset.html',locals())

def update_asset(request,asset_id):
    if request.method == "POST":
        return HttpResponse("ok")
    else:
        obj = Asset_List.objects.filter(id=asset_id).first()
        print obj
        obj = Asset_Form({"ip_add":obj.ip_add,"server_name":obj.server_name,
            "cpu":obj.cpu,"mem":obj.mem,"hard":obj.hard,
            "region":obj.region,"position":obj.positon,
            "cabinet":obj.cabinet,"shelf_time":obj.shelf_time,
            "description":obj.description}
        )
        print type(obj)
        asset_id = {"id":asset_id}
        return  render(request,'myarticle/update_asset.html',locals())