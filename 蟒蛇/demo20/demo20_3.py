# -*- coding:utf-8 -*-
import re
#任务：将现行的《论语》读本进行处理与提纯 1）由文件 论语.txt去掉注释部分得到论语-原文.txt；
# 2）去掉文件 论语-原文.txt引用标号部分得到文件  论语-提纯原文.txt
with open("论语.txt","r",encoding="utf-8") as f:
    a=f.read()
    f.seek(0)
    t=f.readlines()
    b=re.findall(r"[原][文].\s{4}.*\s{4}[^【]*",a)
    # print(b)
    with open("论语原文.txt",'w',encoding='utf-8') as w:
        with open("论语提纯原文.txt",'w',encoding='utf-8') as w1:
            for i in b:
                w.write(i[5:-3])
                for j in range(20):
                    i= i.replace("(" + str(j) + ")", "")
                i=i.replace("\n","")
                i=i.replace(" ","")
                w1.write(i[3:]+"\n")