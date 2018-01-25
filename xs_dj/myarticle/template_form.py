#!/usr/bin/env python
#coding:utf-8

from django.forms import  fields
from  django import  forms
from django.forms import  widgets
from models import  Server,Userlogin
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

class Asset_Form(forms.Form):
    ip_add = fields.GenericIPAddressField(required=True,error_messages={
        "GenericIPAddressField":"IP地址格式不对",
        "required":"IP地址不能为空"
    },
        initial="请输入IP地址"
    )
    server_name = fields.CharField(max_length=32,required=True,error_messages={
        "required":"承载服务不能为空",
        "max_length":"服务名称不能超过32位",
    },
    widget = widgets.Select()
   )
    cpu = fields.CharField()
    mem = fields.CharField()
    hard = fields.CharField()
    region = fields.CharField(required=True,error_messages={"required":"所在区域不能为空"})
    position = fields.CharField(required=True,error_messages={"required":"具体地址不能为空"})
    cabinet = fields.CharField(required=True,error_messages={"required":"具体机柜位置不能为空"})
    shelf_time = fields.DateField(required=True,error_messages={"required":"上架时间不能为空","DateField":"时间格式不对"},
                                  label_suffix="注：格式 2014-08-01")
    description = fields.CharField(
        required=False,
        widget=forms.Textarea
    )

    def __init__(self,*args,**kwargs):
        super(Asset_Form,self).__init__(*args,**kwargs)
        self.fields["server_name"].widget.choices = \
        Server.objects.values_list("id", "server_name")

class Register_Form(forms.Form):
    username = fields.CharField(
        required=True,
        min_length=4,
        max_length=20,
        widget=widgets.TextInput(attrs={"class":"form-control","id":"inputUser3",'placeholder':"用户名"}),
        error_messages={
            "required":"用户名不能为空",
            "min_length":"用户名长度不小于4位",
            "max_length":"用户名长度不能超过20位"
        }
    )
    password = fields.CharField(
        required=True,
        min_length=8,
        max_length=18,
        widget=widgets.PasswordInput(attrs={"class":"form-control","id":"inputPassword3","placeholder":"密码:必须包含字母数字特殊字符"},render_value=True),
        validators=[
            RegexValidator(r'((?=.*\d))^.{6,12}$', '必须包含数字'),
            RegexValidator(r'((?=.*[a-zA-Z]))^.{6,12}$', '必须包含字母'),
            RegexValidator(r'((?=.*[^a-zA-Z0-9]))^.{6,12}$', '必须包含特殊字符'),
            RegexValidator(r'^.(\S){6,10}$', '密码不能包含空白字符'),
        ],  # 用于对密码的正则验证
        error_messages={
            "required":"密码不能为空",
            "min_length":"密码长度不小于8位",
            "max_length":"密码长度不大于18位"
        }
    )
    pwd_again = fields.CharField(
        # render_value会对于PasswordInput，错误是否清空密码输入框内容，默认为清除，我改为不清楚
        widget=widgets.PasswordInput(attrs={'class': "form-control", 'placeholder': '请再次输入密码!',"id":"inputEnterPassword3"}, render_value=True),
        required=True,
        # strip=True,
        error_messages={'required': '请再次输入密码!', }

    )
    email = fields.EmailField(
        required=True,
        widget=widgets.TextInput(attrs={'class': "form-control", 'placeholder': '邮箱!',"id":"inputemail3"}),
        error_messages={
            "required":"邮箱不能为空",
            "invalid":"请输入正确的邮箱格式"
        }
    )

    # 写几个方法来检测数据库中是否存在，可以单独放其他写也是一样的
    def check_username(self):
        # self就是这个对象本身，在实例化的时候接收的参数就是一个查询集，所以存在cleaned_data方法
        user = self.cleaned_data.get("username")
        count = Userlogin.objects.filter(username=user).count()
        # 定制数据格式返回前端
        if count:
            result = {"user":"用户名已经存在"}
            return result
           # raise ValidationError("用户名已经存在")
        return True

    def check_two_pwd(self):
        pwd = self.cleaned_data.get("password")
        twice = self.cleaned_data.get("pwd_again")
        if pwd != twice:
            result = {"pwd":"两次密码输入的不一致"}
            return  result
        return  True

    def check_email(self):
        email = self.cleaned_data.get("email")
        count = Userlogin.objects.filter(email=email)
        if count:
            result = {"email":"此邮箱已注册"}
            return  result
        return True