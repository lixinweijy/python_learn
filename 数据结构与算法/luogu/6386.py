# -*- coding:utf-8 -*-
a=input().split()
a1=int(a[0])
a2=int(a[1])
a3=int(a[2])
a4=int(a[3])
b=input().split()
for i in range(3):
    flag=0
    c=int(b[i])%(a1+a2)
    if c<=a1:
        flag+=1
    d=int(b[i])%(a3+a4)
    if d<=a3:
        flag+=1
    if c==0:
        flag-=1
    if d==0:
        flag-=1
    if flag==0:
        print("none")
    elif flag==1:
        print("one")
    else:
        print("both")