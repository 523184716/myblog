# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from io import  BytesIO
from models import *
from myarticle.utils.user_secret import usersecret
# Create your views here.
from template_form import *
from myarticle.utils import create_image,create_images

def index(request):
    obj = Article.objects.all()
    return render(request,'myarticle/index.html',locals())


def login(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        print request.session
        request.session[password] = password
        if username and password:
            password = usersecret(password)
            # userlogin.objects.create(username=username, password=password)
            count = Userlogin.objects.filter(username=username, password=password)

            if count:
                # array = userlogin.objects.all().values("id","username","password","create_date")
                # array = list(array)
                # for i in array:
                #     print i.username,i.password, i.create_date
                # array_dic = {"array":array}
                # return  HttpResponse(json.dumps(array,cls=CJSONEncoder))
                return redirect('/myarticle/index', permanent=True)
            else:
                ret = {"result": "抱歉您的用户名不存在或密码不正确"}
                # return HttpResponse(json.dumps(ret))
                return render(request, 'myarticle/login.html', ret)
        else:
            ret = {"us_result": "请输入用户名和密码"}
            return render(request, 'myarticle/login.html', ret)
    else:
        return render(request, 'myarticle/login.html',locals())
    # return  render(request,'myarticle/login.html',locals())

def article(request,article_id):
    obj = Article.objects.filter(id=article_id)
    return render(request,'myarticle/article_display.html',locals())

def asset(request):
    obj = Asset_List.objects.all()
    return  render(request,'myarticle/asset_list.html',locals())

def add_asset(request):
    if request.method == "POST":
        # 提交数据至数据，前提是先验证数据的合法性
        obj = Asset_Form(request.POST)
        if obj.is_valid():
            print obj.cleaned_data
            obj = obj.cleaned_data
            # id = Server.objects.filter(server_name=obj["server_name"]).values("id")[0]["id"]
            # obj["server_name"] = id
            # print obj
            print obj
            Asset_List.objects.create(**obj)
            return redirect("myarticle/asset_list")
        else:

            return render(request, 'myarticle/add _asset.html', locals())
    else:
        obj = Asset_Form()
        # 纯粹的加载一个添加数据的页面
        return  render(request,'myarticle/add _asset.html',locals())

def update_asset(request,asset_id):
    if request.method == "POST":
        print request.POST
        obj = request.POST
        print obj["csrfmiddlewaretoken"]
        # del  obj["csrfmiddlewaretoken"]
        # request获取到的是查询集，不允许修改，先验证提交数据的合法性
        obj = Asset_Form(obj)
        if obj.is_valid():
            # 清除表单用户填写之外的数据，方便载入数据库，顺便转成字典格式
            obj = obj.cleaned_data
            #由于服务这里是通过外键关联的形式，所以得先获取id才能导入数据
            id = Server.objects.filter(server_name=obj["server_name"]).values("id")[0]["id"]
            obj["server_name"] = id
            Asset_List.objects.filter(id=asset_id).update(**obj)
            return redirect("myarticle/asset_list")
        else:
            return render(request, 'myarticle/update_asset.html', locals())
    else:
        #根据访问的id从数据库获取数据
        obj = Asset_List.objects.filter(id=asset_id).first()
        #把数据加载进表单中
        obj = Asset_Form({"ip_add":obj.ip_add,"server_name":obj.server_name,
            "cpu":obj.cpu,"mem":obj.mem,"hard":obj.hard,
            "region":obj.region,"position":obj.position,
            "cabinet":obj.cabinet,"shelf_time":obj.shelf_time,
            "description":obj.description}
        )
        asset_id = {"id":asset_id}
        # 表单数据加载进新的页面中，这样修改数据就是之前的那天数据
        return  render(request,'myarticle/update_asset.html',locals())

def user_register(request):
    if request.method == "GET":
        obj = Register_Form()
        return  render(request,'myarticle/user_register.html',locals())
    else:
        obj = Register_Form(request.POST)
        if obj.is_valid():
            pass
        else:
            return  render(request,'myarticle/user_register.html',locals())


def create_code_img(request):
    f = BytesIO() #直接在内存开辟一点空间存放临时生成的图片
    # 调用check_code生成照片和验证码
    img, code = create_images.Create_image()
    print img , code
    request.session['check_code'] = code #将验证码存在服务器的session中，用于校验
    img.save(f,'PNG') #生成的图片放置于开辟的内存中
    # print f.getvalue()
    return HttpResponse(f.getvalue())  #将内存的数据读取出来，并以HttpResponse返回