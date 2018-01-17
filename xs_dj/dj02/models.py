# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import  forms
# Create your models here.

class userlogin(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=256)
    create_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return  self.username

class assets_list(models.Model):
    server_name = models.CharField(max_length=50,verbose_name="服务名")
    server_IP = models.GenericIPAddressField(verbose_name="服务器地址")
    cpu = models.CharField(max_length=10,verbose_name="cpu")
    mem = models.CharField(max_length=20,verbose_name="内存")
    system = models.CharField(max_length=20,verbose_name="操作系统")
    region = models.CharField(max_length=30,verbose_name="机房区域")
    create_date = models.DateTimeField(verbose_name="上架日期")
    remarks = models.TextField(max_length=200,verbose_name="备注")

    def __unicode__(self):
        return  self.server_name

class uaseradmin(models.Model):
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1,choices=((1,"man"),(2,"women"),(3,"zhong")))

    def __unicode__(self):
        return self.name

class serveradmin(models.Model):
    user = models.CharField(max_length=30)
    level = models.CharField(max_length=30)

    def __unicode__(self):
        return  self.user

class server(models.Model):
    name = models.CharField(max_length=30)
    IP = models.GenericIPAddressField()
    grade = models.ForeignKey(serveradmin)

    def __unicode__(self):
        return  self.name

# class UploadFileForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     file = forms.FileField()
#
#     def __unicode__(self):
#         return  self.title

class Book(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    pub_date = models.DateTimeField()
    author = models.ManyToManyField("Author")

    def __unicode__(self):
        return  self.name

class Author(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __unicode__(self):
        return  self.name
