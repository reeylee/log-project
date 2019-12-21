from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import datetime
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from logic import create_handle_log
from constants import LOGPATH
# Create your views here.
from .models import Logs
def create_log(request):
    f = open("ddns.log")               # 返回一个文件对象   
    line = f.readline()               # 调用文件的 readline()方法   
    while line:   
        log = eval(line)
        logs = Logs(c_date=log['date'], code=log['code'], status=log['msg'].encode('utf-8'))
        logs.save()
        line = f.readline()   
   
    f.close()

    # logs = Logs(c_date='2019-1-1 10:54:32.43455', code=0, status='ok')
    # logs.save()
    return HttpResponse('ok')

def get(request):
    logs = Logs.objects.all()
    paginator = Paginator(logs, 20)  #设置每一页显示几条  创建一个panginator对象
    
    try:
        current_num = int(request.GET.get('page',1))  #当你在url内输入的?page = 页码数  显示你输入的页面数目 默认为第2页
        logs = paginator.page(current_num)
    except EmptyPage:
            logs = paginator.page(1)  #当你输入的page是不存在的时候就会报错

    if paginator.num_pages > 11:  # 如果分页的数目大于11
            if current_num - 5 < 1:  # 你输入的值
                pageRange = range(1, 11)  # 按钮数
            elif current_num + 5 > paginator.num_pages:  # 按钮数加5大于分页数
                pageRange = range(current_num - 5, current_num + 1)  # 显示的按钮数

            else:
                pageRange = range(current_num - 5, current_num + 6)  # range求的是按钮数   如果你的按钮数小于分页数 那么就按照正常的分页数目来显示

    else:
        pageRange = paginator.page_range()  # 正常分配

    return render(request, 'demo.html', locals())

def search(request):
    # print(request.method)
    search = request.POST.get('search')
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date') + ' 23:59:59.99999'
    # print(end_date)
    logs = Logs.objects.filter(c_date__range=(start_date, end_date)).filter(status__contains=search)
    logs = serializers.serialize("json",logs)
    data = {"data":logs}
    return JsonResponse(data)

def nearby_logs(request):
    # 查找相邻的log日志
    id = eval(request.POST.get('id'))
    start_id= id-5 if id-5 >=0 else 0
    end_id = id+5 
    logs = Logs.objects.filter(pk__range=(start_id, end_id))
    logs = serializers.serialize("json",logs)
    data = {"data":logs}
    print(data)
    return JsonResponse(data)

def get_handel_log(request):
    create_handle_log()
    return 
