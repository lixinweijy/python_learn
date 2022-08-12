# -*- coding:utf-8 -*-
import re
import jieba
import urllib.request
#获取三国中人名与字  存在一个列表里面  以这样的形式[[名,字],[名,字],[名,字],[名,字]]
url="https://zhidao.baidu.com/question/114631954.html"
resp=urllib.request.urlopen(url)
html=resp.read().decode("gbk")
mz=re.findall(r"三国人物大全（魏）.*",html)[0]
mz=re.findall(r"<br />.{10}",mz)
mz.pop(0)
#由于原本信息中每条信息后面还有籍贯之类的，用这个for循环去掉无关紧要的东西，不过有的人名里面没有字，不过无关大雅，因为没有字的都是不出名的
k=[]
for i in range(len(mz)):
    mz[i]=jieba.lcut(mz[i][6:])
    mz[i][1]=mz[i][2]
    while len(mz[i])>2:
        mz[i].pop()
    if ord(mz[i][0][0])<200 or ord(mz[i][0][0])==65288 or len(mz[i][0])==1 or len(mz[i][1])==1:
        k.append(i-len(k))
mz[1]=["刘备","玄德"]
mz.append(["关羽","云长"])
for i in k:
    mz.pop(i)
zidian={}
num={}
# print(mz)
with open("三国演义（原）.txt","r",encoding='utf-8') as f:
    all_1=f.read()
with open("三国演义_1.txt","r",encoding="utf-8") as r:
    all=r.readlines()

def tool(a,b,c):
    index_mz = all_1.find(b)
    txt_before = all_1[index_mz- 300:index_mz]
    if a[0] in txt_before or a[1] in txt_before:
        zidian[a[0]]=zidian.get(a[0],0)+1
        num[a[0]]=num.get(a[0],0)+len(c[1])
    elif a[0][-1:] in txt_before:
        tool(a,txt_before,c)
for i in all:
    d=i.replace('"',' ').split()
    # print(d)
    for k in range(len(mz)):
        if mz[k][0] in d[0] or mz[k][1] in d[0]:#名字都在里面
            zidian[mz[k][0]]=zidian.get(mz[k][0],0)+1
            num[mz[k][0]]=num.get(mz[k][0],0)+len(d[1])
            break
        elif mz[k][0][-1:] in d[0]:#只有名的最后一个字在里面
            tool(mz[k],i,d)
            # break
a=list(zidian.items())
a.sort(key=lambda x:x[1],reverse=True)
print(a)
print(f"说话句数最多的是:{a[0][0]},共说了{a[0][1]}句话")
b=list(num.items())
b.sort(key=lambda x:x[1],reverse=True)
print(f"说话字数最多的是:{b[0][0]},共说了{b[0][1]}个字")
print(b)