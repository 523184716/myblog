# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect,HttpResponse
from auth_secret.user_secret import usersecret
from models import userlogin,assets_list,server,uaseradmin,serveradmin,Book,Author
import  json
import  datetime
from datetime import  date
from django.db.models import  Q,Avg,Max,Min,Count,Sum
from django import  forms
import  os
import  chardet
from django.contrib.auth.models import User
from django.forms import  ModelForm
from django.contrib.sessions.middleware import  SessionMiddleware
from django.contrib.sessions.models import  Session
# Create your views here.
from  django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET,require_http_methods,require_POST,require_safe
# @csrf_exempt
def index(request):
    now = datetime.datetime.now()
    List = [i for i in range(10)]
    Dict = {i:i for i in range(10)}
    myfirstonetest = "aaaaaaaaaa"
    testdict = {"num":10,"page":"my name is page","python":"python","current_date":now,"def":""}
    return  render(request,'dj02/index1.html',locals())

class CJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj,date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self,obj)

# @csrf_exempt
# @require_POST
def login(request):
    if request.method == "POST":
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        print request.session
        request.session[password] = password
        if username and password:
            password = usersecret(password)
            # userlogin.objects.create(username=username, password=password)
            count = userlogin.objects.filter(username=username,password=password)
            print count
            if count:
                # array = userlogin.objects.all().values("id","username","password","create_date")
                # array = list(array)
                # for i in array:
                #     print i.username,i.password, i.create_date
                # array_dic = {"array":array}
                # return  HttpResponse(json.dumps(array,cls=CJSONEncoder))
                print "ok"
                return redirect('/dj02/index',permanent=True)
            else:
                ret = {"result":"抱歉您的用户名不存在或密码不正确"}
                # return HttpResponse(json.dumps(ret))
                return render(request,'dj02/login.html',ret)
        else:
            ret = {"us_result":"请输入用户名和密码"}
            return  render(request,'dj02/login.html',ret)
    # formtest = UploadFileForm()
    # formtest = ContactForm()
    return  render(request, 'dj02/login.html')

def assets(request):
    assets_data = assets_list.objects.all()
    return render(request,'dj02/assets.html',{"assets_list":assets_data})

def report(request):
    return  render(request,'dj02/report.html')

def add(request,num):
    # example = assets_list(server_name="edi1",server_IP="172.16.1.17",cpu="4",mem="8G",
    #                       system="centos7.1",region="广东电信",create_date="2018-01-09",remarks="")
    # example.save()
    # for i in request.POST:
    #     assets_list.objects.create(server_name=i.server_name,server_IP=i.server_IP,cpu=i.cpu,mem=i.mem,system=i.system,
    #                                region=i.region,create_date=i.create_date,remarks=i.remarks)
    # obj1 = Book(name="openstack",price="45",pub_date="2016-02-08")
    # obj2 = Book(name="docker", price="36", pub_date="2016-02-08")
    # Book.objects.create(name="python",price="38",pub_date="2015-01-22")
    # Author.objects.create(name="while",age=35)
    # Author.objects.create(name="django", age=36)
    # Author.objects.create(name="for", age=30)
    # Author.objects.create(name="while", age=29)
    # data = Book.objects.filter(author__name="while").values("name","price")
    # print data
    # obj = Author.objects.filter(name="head")
    # Book.objects.get(name="php").author.add(*obj)
    # Book.objects.get(name="python").author.add(*(Author.objects.all()))
    # obj = Book.objects.filter(name="php").values("name","price","author__name","author__book__name")
    # print obj
    # obj = Book.objects.filter(Q(name="python") & Q(author__name="head"))
    # obj = Book.objects.get(name="python").author.filter(name="head").delete()
    # 查所有老师分别所出书籍的总价
    obj1 = Book.objects.values("author__name").annotate(names=Sum("price"))
    print obj1
    # 查所有老师所出书籍最贵的书
    obj2 = Book.objects.values("author__name").annotate(names=Max("price"))
    print obj2
    # 查询所有老师所出书的平均价格
    obj3 = Author.objects.values("name").annotate(names=Avg("book__price"))
    print obj3
    # 查询while老师和head老师所出书籍总数
    obj4 = Author.objects.filter(Q(name="while") | Q(name="head")).aggregate(Count("book__name"))
    print obj4
    return HttpResponse("添加成功")

def delete(request):
    # servername = request.POST.get("server_name",None)
    assets_list.objects.filter(id=1).delete()
    return HttpResponse("删除成功")

# @require_POST
def modify(request):
    # modi_data = assets_list.objects.get(server_name="精灵")
    # modi_data.cpu = 12
    # modi_data.save()
    # modi_data.delete()
    # assets_list.objects.filter(server_name="精灵3").update(cpu="16")
    # search = assets_list.objects.filter(server_name__startswith="精灵")[0].server_name
    # print search
    return HttpResponse("修改成功")

def select(request):
    # relate_select = server.objects.filter(grade__user="admin").delete()
    # print relate_select
    # rever_select = serveradmin.objects.filter(server__name="cm1").values("user","level")
    # print rever_select
    # morefilter = serveradmin.objects.filter(server__name="cm1").filter(server__IP="172.16.1.11")
    # print morefilter
    # orselect = server.objects.filter(Q(name="cm1")|Q(name="edi1")).values("name")
    # print orselect
    # copytable = serveradmin(user="test",level="普通用用户")
    # copytable.save()
    # copytable.pk = None
    # copytable.save()
    # copytable = serveradmin.objects.get(user="root")
    # data = copytable.server_set.all()
    # print data
    # print copytable.server_set.count()
    print request.session["123456"]
    avg = server.objects.all().aggregate(Avg("grade"),Max("grade"),Min("grade"))
    print avg
    data = server.objects.filter(name="cm1").values("name","IP","grade__user","grade__level")
    print data
    print avg.get("grade__avg")
    return  redirect('/dj02/asset_allocate')

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

def formget(request):
    print request.FILES.get("test")
    obj = request.FILES.get("test")
    print obj.size
    # print obj.name
    with open(os.path.join(os.path.dirname(__file__),"{}".format(obj)),"wb") as file:
        for i in obj.chunks():
            print "ok"
            file.write(i)
    # form = UploadFileForm(request.POST, request.FILES)

    return  redirect('/dj02/asset_allocate')