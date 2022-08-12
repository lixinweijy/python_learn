# -*- coding:utf-8 -*-
d2={}
d3={}
fo=open('商品数量库.txt','w',encoding='utf-8')
with open('商品目录.txt', 'r',encoding='utf-8') as txt:
    for i in range(len(txt.readlines())):
        a=txt.readline()
        b= list(a.items())
while(1):
    a=input()
    if a=='n':
        break
    d3[a]=d2.get(a,0)+1
    print(d3)
fo.write(str(d3))
fo.close()