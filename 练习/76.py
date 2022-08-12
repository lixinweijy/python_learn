# -*- coding:utf-8 -*-
import requests
import re
import time
for i in range(5):
    url="https://image.baidu.com/search/acjson?tn=resultjson_com&logid=8290536107600066764&ipn=rj&ct=201326592&is=&fp=result&fr=ala&word=%E5%A4%B4%E5%83%8F&cg=head&queryWord=%E5%A4%B4%E5%83%8F&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&expermode=&nojc=&isAsync=&pn="+str(i)+"&rn=30&gsm=96&1649124487150="
    header={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}
    resp=requests.get(url,headers=header)
    resp=resp.text
    a=re.findall("(?<=middleURL\":\").*?(?=\")",resp)
    for i in range(len(a)):
        url1=a[i]
        resp=requests.get(url1,headers=header)
        with open("img/"+str(time.time())+".png","wb") as f:
            f.write(resp.content)