# -*- coding:utf-8 -*-
#任务：从文件data1.txt中统计二字词的词频，并显示前10名
import jieba
z={}
with open("data1.txt",'r',encoding="utf-8") as f:
    a=f.readlines()
    for i in a:
        k=jieba.lcut(i, cut_all = True)
        for j in k:
            if len(j)==2:
                z[j]=z.get(j,0)+1
zz=list(z.items())
zz.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    print("{}:{:>2s}".format(zz[i][0],str(zz[i][1])))
