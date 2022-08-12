# -*- coding:utf-8 -*-
import requests
"""
request(url)            构造一个请求
get(url,params=None)    发送get请求  params为请求参数
post()                  发送post请求
head()                  获取html头部信息
put()                   发送put请求
patch()                 提交局部修改的请求
delete()                提交删除的请求
"""

#结果为response对象
"""
response属性或方法:
status_code             响应状态码
content                 把response对象转换为二进制数据
text                    转换为字符串数据
encoding                定义response对象的编码
cookies                 获取请求后的cookie
url                     获取请求的网址
json()                  内置的json解码器
headers                 以字典对象储存服务器响应头，字典键不区分大小写
"""
#发送不带参数的get请求
import requests
url="http://www.baidu.com"
resp=requests.get(url)
#设置响应的编码格式
resp.encoding='utf-8'
cookie=resp.cookies  #获取请求后的cookie信息
header=resp.headers
print("响应的状态码:",resp.status_code)
print("请求后的cookie:",cookie)
print("获取请求的网址",resp.url)
print("响应头:",header)
print("响应内容:",resp.text)

#带参数的get请求
url1="https://www.so.com/s"
params={"q":"python"}
resp=requests.get(url1,params=params)
resp.encoding='utf-8'
print(resp.text)