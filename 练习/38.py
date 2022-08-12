# -*- coding:utf-8 -*-
a=input("").split()
b=int(a[1])
c=0
fuhao=input("")
num=input("").split()
for i in range(b):
    z=[]
    modify=input("").split()
    num[int(modify[0])-1]=modify[1]
    for i in num:
        z.append(i)
    k=0
    for j in range(len(fuhao)):
        if fuhao[j:j+1]=="*":
            num[k]=int(num[k])*int(num[k+1])
            num.pop(k+1)
            k-=1
        k+=1
    for o in range(len(num)):
        c+=int(num[o])
    print(c)
    c=0
    num=z
