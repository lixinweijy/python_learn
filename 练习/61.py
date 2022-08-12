# -*- coding:utf-8 -*-
with open("a.txt",'rb') as a:
    a.seek(4)
    print(a.tell())
    a.seek(-1,1)
    print(a.tell())
