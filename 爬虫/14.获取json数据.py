# -*- coding:utf-8 -*-
import requests
# url="https://image.baidu.com/search/acjson?tn=resultjson_com&logid=12987887312019178882&ipn=rj&ct=201326592&is=&fp=result&fr=ala&word=%E7%BE%8E%E5%A5%B3&cg=girl&queryWord=%E7%BE%8E%E5%A5%B3&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&expermode=&nojc=&isAsync=&pn=120&rn=30&gsm=78&1648548554538="
# resp=requests.get(url)
# json_data=resp.json()
# print(json_data)


url='https://www.baidu.com/img/flexible/logo/pc/result@2.png'
resp=requests.get(url)
# json_1=resp.json()
with open("img.png",'wb') as file:
    file.write(resp.content)

# print(json_1)
# print(resp.content)