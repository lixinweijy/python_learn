# -*- coding:utf-8 -*-
from pyecharts.charts import Bar
z=[]
with open("data4.txt",'r',encoding="gbk") as r:
    x=list(r)
    sum=0
    for i in range(1,len(x)):
        k=x[i].split()
        sum=int(k[1])+int(k[2])+int(k[3])
        if (int(k[1])>85 and int(k[2])>85 and int(k[3])>85) or sum>260:
            print(k[0],"\t优秀")
        elif(int(k[1])>60 and int(k[2])>60 and int(k[3])>60) or sum>180:
            print(k[0], "\t合格")
        else:
            print(k[0], "\t不合格")
        z.append(k[0])
        z.append(sum)
Bar().add_xaxis([z[2*i] for i in range(len(z)//2-1)]).add_yaxis("总分",[z[2*i+1] for i in range(len(z)//2-1)]).render("总分表.html")