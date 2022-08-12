# -*- coding:utf-8 -*-
"""自定义Web框架"""
import time

from functools import wraps
import pymysql
#定义一个路由表
route_list=[]
# route_list={
#     # ('/index.html',index),
#     # ('/5.html',second)
# }

# 定义一个带参数装饰器
def route(request_path): #参数就是URL请求
    def add_route(func):
        #添加路由到路由表
        route_list.append((request_path,func))
        @wraps(func)
        def invoke(*arg,**kwargs):
            #调用我们指定的处理函数，并且返回结果
            return func()
        return invoke
    return add_route

#处理动态资源请求的函数
def handle_request(params):
    request_path=params['request_path']
    for path,func in route_list:
        if request_path==path:
            return func()
    else:
        return page_not_found()
    # if request_path=='/index.html':#当前的请求路径有与之对应的动态响应,当前框架，我只开发了index.html的功能
    #     response=index()
    #     return response
    # elif request_path=="/5.html":#第二个页面
    #     return second()
    # else:
    #     #没有动态资源，返回404页面
    #     return page_not_found()

#当前index函数，专门处理index.html请求
@route("/index.html")
def index():
    #需求：从数据库中取得所有的电影数据，并且动态展示
    # data=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #1.从MySql数据库中查询数据
    conn=pymysql.connect(host='localhost',port=3306,user='root',password='root',db='t_movies',charset='utf8')
    cursor=conn.cursor()
    cursor.execute('select * from t_movies')
    result=cursor.fetchall()
    print("数据库内容",result)

    datas=''
    for row in result:
        datas+="""
        <tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s 亿</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td><input type='button' value='删除'></td>
        </tr>
        """%row
    print(datas)

    # 把查询的数据转化为动态内容
    with open('template/index.html','r',encoding='utf-8') as f:
        response_body=f.read()
    response_body=response_body.replace("{%datas%}",datas)
    response_first_line = 'HTTP/1.1 200 OK\r\n'
    response_header = 'Server: lxw_server\r\n'
    response = (response_first_line + response_header + "\r\n" + response_body).encode("utf-8")
    return response

#当前second函数，用来处理5.html的动态请求
@route("/5.html")
def second():
    # 需求，在页面中动态显示时间
    # data = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open('template/5.html', 'r', encoding='utf-8') as f:
        response_body = f.read()
    # response_body = response_body.replace("{%datas%}", data)
    response_first_line = 'HTTP/1.1 200 OK\r\n'
    response_header = 'Server: lxw_server\r\n'
    response = (response_first_line + response_header + "\r\n" + response_body).encode("utf-8")
    return response

def page_not_found():
    with open("static/404.html",'rb') as f:
        response_body=f.read()
    response_first_line = 'HTTP/1.1 404 Not Found\r\n'
    response_header = 'Server: lxw_server\r\n'
    response = (response_first_line + response_header + "\r\n").encode("utf-8") + response_body
    return response
