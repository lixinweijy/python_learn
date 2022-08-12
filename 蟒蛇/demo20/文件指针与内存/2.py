# -*- coding:utf-8 -*-
import requests
import re
import time
"""
get(url,params=None)    发送get请求  params为请求参数
text                    转换为字符串数据
url                     获取请求的网址
headers                 以字典对象储存服务器响应头，字典键不区分大小写
"""
for i in range(1):
    url="https://image.baidu.com/search/acjson?tn=resultjson_com&logid=11914674459893937713&ipn=rj&ct=201326592&is=&fp=result&fr=ala&word=%E7%BE%8E%E5%A5%B3&cg=girl&queryWord=%E7%BE%8E%E5%A5%B3&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&expermode=&nojc=&isAsync=&pn="+str(i)+"&rn=30&gsm=42&1648727533943="
    header={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }
    resp=requests.get(url,headers=header)
    resp=resp.text
    resp1=re.findall("(?<=middleURL\":\").*?(?=\")",resp)
    for j in range(len(resp1)):
        url1=resp1[j]
        resp = requests.get(url1, headers=header)
        print("1")
        with open("img/"+str(time.time())+".png","wb") as w:
            w.write(resp.content)