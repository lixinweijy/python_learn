# -*- coding:utf-8 -*-
with open("三国演义_1.txt","r",encoding="utf-8") as r:
    all=r.readlines()
    for i in all:
        if i[0]=="\"":
            i=i[1:]
        a=i.count("\"")
        if a!=2:
            print(i)
