# -*- coding:utf-8 -*-
import urllib.request
import urllib.error
url="http://www.google.com"  #错误的网址
try:
    resp=urllib.request.urlopen(url)
except urllib.error.URLError as e:
    print(e.reason)
#urllib.error.HTTPError  用于捕获由urllib.request产生的异常，使用reason属性返回错误原因

#urllib.error.HTTPError  用于处理HTTP与HTTPS请求的错误，它有三个属性
"""
code:请求返回的状态码
reason:返回错误的原因
headers:请求返回的响应头信息
"""

url="https://movie.douban.com/"
try:
    reap=urllib.request.urlopen(url)
except urllib.error.HTTPError as e:
    print("原因：",e.reason)
    print("响应状态码:",str(e.code))
    print("响应头数据",e.headers)