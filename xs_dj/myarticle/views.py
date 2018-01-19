# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import *
# Create your views here.

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