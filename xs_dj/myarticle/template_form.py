#!/usr/bin/env python
#coding:utf-8

from django.forms import  fields
from  django import  forms
class Asset_Form(forms.Form):
    ip_add = fields.GenericIPAddressField(required=True,error_messages={
        "GenericIPAddressField":"IP地址格式不对",
        "required":"IP地址不能为空"
    })
    server_name = fields.CharField(max_length=32,required=True,error_messages={
        "required":"承载服务不能为空",
        "max_length":"服务名称不能超过32位"
    })
    cpu = fields.CharField()
    mem = fields.CharField()
    hard = fields.CharField()
    region = fields.CharField(required=True,error_messages={"required":"所在区域不能为空"})
    position = fields.CharField(required=True,error_messages={"required":"具体地址不能为空"})
    cabinet = fields.CharField(required=True,error_messages={"required":"具体机柜位置不能为空"})
    shelf_time = fields.DateField(required=True,error_messages={"required":"上架时间不能为空","DateField":"时间格式不对"})
    description = fields.TextInput()