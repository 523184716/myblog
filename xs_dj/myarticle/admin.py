# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *
# Register your models here.

# 注册应用到admin管理后台之后显示的数据列表以及添加其他一些展示，比如：search，过滤条件
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name","email","phone")

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title","author","pub_date")

class AssetAdmin(admin.ModelAdmin):
    list_display = ("ip_add","server_name","shelf_time")
    list_filter = ("shelf_time",)

class ServerAdmin(admin.ModelAdmin):
    list_display = ("server_name","server_port","access_type")
    list_filter = ("server_name","server_port","access_type")

# 正式把model注册到admin后台
admin.site.register(Author,AuthorAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Asset_List,AssetAdmin)
admin.site.register(Server,ServerAdmin)