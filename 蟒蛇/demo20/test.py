# -*- coding:utf-8 -*-
with open("2.txt",'r',encoding="utf-8") as f:
    a=f.read()
    print("上:",a.count("上"))
    print(r"\n:",a.count("\n"))
    print("中:", a.count("中"))
    print("，:", a.count("，"))
