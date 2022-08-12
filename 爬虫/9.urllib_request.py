# -*- coding:utf-8 -*-
import urllib.request

url="https://www.jd.com/?cu=true&utm_source=c.duomai.com&utm_medium=tuiguang&utm_campaign=t_16282_26173494&utm_term=b3029df83b8c49d88674646be0bcea5c"

#发送请求
resp=urllib.request.urlopen(url)
html=resp.read().decode("utf-8")
# print(html)

"""
urlopen(url,data=None,[timeout,]*,cafile=None,capath=None,cadefault=False,context=None)
data:默认值为None，urllib判断参数data是否为None从而区分请求方式。
参数为None,则表示请求方式为Get，反之为Post，发送Post请求。
参数data以字典形式存储数据，并将参数data由字典类型转换成字节类型才能完成Post请求
"""
url='https://www.baidu.com'
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55"}
#构建请求对象
req=urllib.request.Request(url,headers=headers)

opener=urllib.request.build_opener()

resp=opener.open(req)
print(resp.read().decode())
