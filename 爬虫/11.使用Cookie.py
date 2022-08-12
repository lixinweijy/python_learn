# -*- coding:utf-8 -*-
"""
为什么使用Cookie:
解决http的无状态性
"""

"""
使用步骤:
实例化MozillaCookieJar(保存cookie)
创建handler对象(cookie的处理器)
创建opener对象
打开网页(发送请求获取响应)
保存cookie文件
"""
import urllib.request
from http import cookiejar

filename="Cookie.txt"

#获取cookie
def get_cookie():
    #(1)实例化一个MozillaCookieJar
    cookie=cookiejar.MozillaCookieJar(filename)
    #(2)创建handler对象
    handler=urllib.request.HTTPCookieProcessor(cookie)
    #(3)创建opener对象
    opener=urllib.request.build_opener(handler)
    #(4)请求网址
    url="https://tieba.baidu.com/index.html"
    resp=opener.open(url)
    #(5)存储cookie文件
    cookie.save()

#读取cookie
def use_cookie():
    #实例化MozillaCookieJar
    cookie=cookiejar.MozillaCookieJar()
    #加载cookie文件
    cookie.load(filename)
    print(cookie)

if __name__ == '__main__':
    get_cookie()
    use_cookie()