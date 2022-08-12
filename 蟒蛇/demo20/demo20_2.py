# -*- coding:utf-8 -*-
#任务：从两份政府工作报告（2018，2019）中找到词频前10名的共有词与特有词
import jieba
z={}
same=[]
particular_2018=[]
particular_2019=[]
def sum(x):
    q={}
    with open(x,'r',encoding="utf-8") as f:
        a=f.readlines()
        for i in a:
            k=jieba.lcut(i, cut_all = True)
            for j in k:
                if len(j)==2:
                    z[j]=z.get(j,0)+1
                    q[j]=q.get(j,0)+1
        kk=list(q.items())
        kk.sort(key=lambda x:x[1],reverse=True)
        kk = [kk[i] for i in range(10)]
        return  kk
k1=sum("政府工作报告2018.txt")
k2=sum("政府工作报告2019.txt")

zz=list(z.items())
zz.sort(key=lambda x:x[1],reverse=True)
zz=[zz[i] for i in range(10)]
for i in k1:
    for j in k2:
        if i[0]==j[0]:
            same.append(i[0])
            break
    else:
        particular_2018.append(i[0])
for i in k2:
    if i[0] not in same:
        particular_2019.append(i[0])

def printf(a,b):
    print(a,end="\t")
    for i in range(len(b)):
        if "十" in a:
            print(b[i][0],end="  ")
        else:
            print(b[i],end="  ")
    print()

printf("总排名前十:",zz)
printf("2018特有词:",particular_2018)
printf("2019特有词:",particular_2019)
printf("共有词:",same)
