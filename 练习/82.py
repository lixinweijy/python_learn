# -*- coding:utf-8 -*-
while True:
    try:
        num=int(input())
        print(f"{num}*{num}*{num}={num ** 3}=",end="")
        for i in range(num):
            if i:
                print("+"+str(num * num -num+1+ i*2), end="")
            else:
                print(str(num * num -num+1+ i*2), end="")
    except:
        break