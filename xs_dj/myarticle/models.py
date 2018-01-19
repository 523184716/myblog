# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from  ckeditor_uploader.fields import  RichTextUploadingField
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=32,verbose_name="文章标题")
    author = models.ForeignKey("Author")
    pub_date = models.DateField(verbose_name="发表日期")
    content = RichTextUploadingField(verbose_name="文章内容")
    img = models.ImageField(upload_to="images",verbose_name="文章图片",blank=True)
    dsecription = RichTextUploadingField(verbose_name="文章摘要",blank=True)

    def __unicode__(self):
        return  self.title

class Author(models.Model):
    name = models.CharField(max_length=32,verbose_name="作者姓名")
    email = models.EmailField(verbose_name="作者邮箱")
    age = models.IntegerField(verbose_name="作者年龄",blank=True,null=True)
    gender_typer = (("man",u"男"),("women",u"女"))
    gender = models.CharField(max_length=3,choices=gender_typer,verbose_name="性别",blank=True)
    phone = models.CharField(max_length=32,verbose_name="手机",blank=True)
    address = models.CharField(max_length=128,verbose_name="地址",blank=True)

    photo = models.ImageField(upload_to="images",verbose_name="文件",blank=True)
    description = RichTextUploadingField(verbose_name="描述",blank=True)

    def __unicode__(self):
        return  self.name

class Asset_List(models.Model):
    ip_add = models.GenericIPAddressField(verbose_name="访问地址")
    server_name = models.ForeignKey("Server")
    cpu = models.CharField(max_length=32,verbose_name="CPU核数",blank=True,null=True)
    mem = models.CharField(max_length=32,verbose_name="内存大小",blank=True,null=True)
    hard = models.CharField(max_length=32,verbose_name="硬盘大小",blank=True,null=True)
    region = models.CharField(max_length=32,verbose_name="所在区域")
    positon = models.CharField(max_length=128,verbose_name="机房地址")
    cabinet = models.CharField(max_length=64,verbose_name="具体机柜位置")
    shelf_time = models.DateField(verbose_name="上架时间")
    description = models.TextField(verbose_name="备注",blank=True,null=True)

    def __unicode__(self):
        return self.ip_add

class Server(models.Model):

    server_name = models.CharField(max_length=32,verbose_name="服务名称")
    server_port = models.CharField(max_length=16,verbose_name="服务端口")
    access_type = models.CharField(max_length=32,verbose_name="访问类别")
    def __unicode__(self):
        return self.server_name