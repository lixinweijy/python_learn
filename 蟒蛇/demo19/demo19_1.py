# -*- coding:utf-8 -*-


file=open('商品基本库文件.txt','w',encoding="utf-8")
a=input("")
b=input("")
d={a:["视听说1",36],b:["高等数学",23]}
file.write(str(d))
file.close()
