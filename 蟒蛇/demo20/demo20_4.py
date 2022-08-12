# -*- coding:utf-8 -*-
#题目：已有文件data4.txt，请将文件内同学的成绩进行统计，并将统计结果写入out4.txt中
#要求：1）三门课都在85以上或总分在260以上为优秀
#2）三门课都在60以上或总分在180以上为合格，其余为不合格
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