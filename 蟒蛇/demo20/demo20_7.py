# -*- coding:utf-8 -*-
import re
import jieba
import urllib.request
url="https://zhidao.baidu.com/question/114631954.html"
resp=urllib.request.urlopen(url)
html=resp.read().decode("gbk")
mz=re.findall(r"三国人物大全（魏）.*",html)[0]
mz=re.findall(r"<br />.{10}",mz)
mz.pop(0)
k=[]
for i in range(len(mz)):
    mz[i]=jieba.lcut(mz[i][6:])
    mz[i][1]=mz[i][2]
    while len(mz[i])>2:
        mz[i].pop()
    if ord(mz[i][0][0])<200 or ord(mz[i][0][0])==65288 or len(mz[i][0])==1:
        k.append(i-len(k))
for i in k:
    mz.pop(i)
zidian={}
num={}
with open("三国演义（原）.txt","r",encoding="utf-8") as r:
    all=r.read()
    all_speak=re.findall(r'[^。]+：".*?"',all)
def woyouyigehanshu1(a,b):
    index_mz = all.find(b)
    txt_before = all[index_mz- 200:index_mz]
    if a[0] in txt_before or a[1] in txt_before:
        zidian[a[0]]=zidian.get(a[0],0)+1
        return 1
    elif a[0][-1:] in txt_before:
        woyouyigehanshu1(a,txt_before)
for i in all_speak:
    c=re.findall(r"[^。]+：\".*?\"",i)
    d=c[0].replace('"',' ').split()
    for j in range(len(d) // 2+1):
        for k in range(len(mz)):
            if mz[k][0] in d[2 * j-1+len(d)%2][:-1] or mz[k][1] in d[2 * j-1+len(d)%2][:-1]:
                zidian[mz[k][0]]=zidian.get(mz[k][0],0)+1
                break
            elif mz[k][0][-1:] in d[2 * j-1+len(d)%2][:-1]:
                woyouyigehanshu1(mz[k],c[0])
a=list(zidian.items())
a.sort(key=lambda x:x[1],reverse=True)
print(a)