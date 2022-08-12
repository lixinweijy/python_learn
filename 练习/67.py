# -*- coding:utf-8 -*-
while 1:
    with open("a.txt","r+") as f:
        f.write(input())
        print(f.read())

