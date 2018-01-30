# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from io import  BytesIO
from models import *
from myarticle.utils.user_secret import usersecret
from template_form import *
from myarticle.utils import create_images
from django.core.paginator import Page,PageNotAnInteger,Paginator,EmptyPage
from utils.base_page import Page_set

def login_Decorator(func):
    def wrapper(request,*args):
        obj = request.session.get("username",None)
        print obj
        if obj:
            return func(request,*args)
        else:
            return redirect('/myarticle/login')
    return wrapper

@login_Decorator
def index(request,index_id=1):
    # 加载首页,获取数据总数
    obj = Article.objects.all().count()
    # print obj
    # 分页实例化
    per_page_item_num = request.session.get("per_page_display_num",None)
    if not per_page_item_num:
        per_page_item_num = 5
    page_set = Page_set(obj,"/myarticle/index/",index_id,per_page_item_num)
    # 获取此页的数据,默认第一页，有带页面参数时才用自带的
    obj = Article.objects.all()[page_set.start_index:page_set.end_index]
    # 获取页码数渲染到前端
    render_page = page_set.page_render
    return render(request,'myarticle/index.html',locals())

def login(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        # 获取账号密码的值，首先判断是否非空
        if username and password:
            # 获取前端验证码以及后端创建的验证码保存在session的值是否相同
            session_code = request.session["check_code"]
            web_code = request.POST.get("check_code")
            if session_code.lower() == web_code.lower():
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

                    # 添加cookie和session
                    request.session["username"]=password
                    request.session.set_expiry(0)
                    # request.session["per_page_display_num"] = 5
                    # 登录成功删除之前保存的分页数据显示初始值
                    per_page_item_num = request.session.get("per_page_display_num", None)
                    if per_page_item_num:
                        del request.session["per_page_display_num"]
                    return redirect('/myarticle/index', permanent=True)
                else:
                    ret = {"result": "抱歉您的用户名不存在或密码不正确"}
                    return render(request, 'myarticle/login.html', ret)
            return render(request,'myarticle/login.html',{"ret":"验证码不正确"})
        else:
            ret = {"us_result": "请输入用户名和密码"}
            return render(request, 'myarticle/login.html', ret)
    else:
        return render(request, 'myarticle/login.html',locals())

@login_Decorator
def article(request,article_id):
    # 根据id检索文章的各项内容展示 在前端
    obj = Article.objects.filter(id=article_id)
    return render(request,'myarticle/article_display.html',locals())

@login_Decorator
def asset(request,index_id=1):
    # 展示资产列表
    print index_id
    obj = Asset_List.objects.all().count()
    per_page_item_num = request.session.get("per_page_display_num", None)
    if not per_page_item_num:
        per_page_item_num = 6
    print "per_page_display_num:",per_page_item_num
    page_set = Page_set(obj, "/myarticle/asset_list/", index_id,per_page_item_num)
    obj = Asset_List.objects.all()[page_set.start_index:page_set.end_index]
    render_page = page_set.page_render
    return  render(request,'myarticle/asset_list.html',locals())

@login_Decorator
def add_asset(request):
    if request.method == "POST":
        # 提交数据至数据，前提是先验证数据的合法性
        obj = Asset_Form(request.POST)
        if obj.is_valid():
            # 在数据有效的前提下从查询集转换成字典，并去除非post用户填写的数据
            obj = obj.cleaned_data
            obj["server_name_id"]=obj["server_name"]
            del obj["server_name"]
            # Asset_List.objects.create(cpu=obj["cpu"],ip_add=obj["ip_add"],mem=obj["mem"],hard=obj["hard"],
            #                           region=obj["region"],position=obj["position"],cabinet=obj["cabinet"],
            #                           shelf_time=obj["shelf_time"],description=obj["description"],server_name_id=4)
            Asset_List.objects.create(**obj)
            return redirect("/myarticle/asset_list")
        else:

            return render(request, 'myarticle/add _asset.html', locals())
    else:
        obj = Asset_Form()
        # 纯粹的加载一个添加数据的页面
        return  render(request,'myarticle/add _asset.html',locals())

@login_Decorator
def update_asset(request,asset_id):
    if request.method == "POST":
        obj = request.POST
        print obj["csrfmiddlewaretoken"]
        # del  obj["csrfmiddlewaretoken"]
        # request获取到的是查询集，不允许修改，先验证提交数据的合法性
        obj = Asset_Form(obj)
        if obj.is_valid():
            # 清除表单用户填写之外的数据，方便载入数据库，顺便转成字典格式
            obj = obj.cleaned_data
            #由于服务这里是通过外键关联的形式，所以得先获取id才能导入数据
            print obj["server_name"]
            # id = Server.objects.filter(server_name=obj["server_name"]).values_list("id")
            # obj["server_name"] = id
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
        # 通过form来渲染注册页面
        obj = Register_Form()
        return  render(request,'myarticle/user_register.html',locals())
    else:
        obj = Register_Form(request.POST)
        if obj.is_valid():
            # 首先判断提交注册的有效性，然后来调用其他的方法来判断数据库中数据是否存在
            result = obj.check_username()
            if result == True:
                result = obj.check_two_pwd()
                if result == True:
                    result = obj.check_email()
                    if result == True:
                        obj = obj.cleaned_data
                        del obj["pwd_again"]
                        obj["password"] = usersecret(obj["password"])
                        Userlogin.objects.create(**obj)
                        return redirect('/myarticle/login')
            return render(request, 'myarticle/user_register.html', locals())
        else:
            return  render(request,'myarticle/user_register.html',locals())

def create_code_img(request):
    f = BytesIO() #直接在内存开辟一点空间存放临时生成的图片
    # 调用check_code生成照片和验证码
    img, code = create_images.Create_image()
    request.session['check_code'] = code #将验证码存在服务器的session中，用于校验
    # print request.session["check_code"]
    img.save(f,'PNG') #生成的图片放置于开辟的内存中
    # print f.getvalue()
    return HttpResponse(f.getvalue())  #将内存的数据读取出来，并以HttpResponse返回

def logout(request):
    # 如果存在session_id，则删除此id
    obj = request.session.get("username",None)
    if obj:
        del request.session["username"]
        return  redirect('/myarticle/login')

def pagecache(request):
    per_page_display_num = request.GET["data"]
    url_path =  request.GET["url_path"]
    print per_page_display_num
    request.session["per_page_display_num"] = per_page_display_num
    return  redirect(url_path)