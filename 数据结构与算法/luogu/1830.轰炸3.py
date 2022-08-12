# -*- coding:utf-8 -*-
a=input("").split()
m=int(a[0])
n=int(a[1])
x=int(a[2])
y=int(a[3])
x1=[0 for i in range(x)]
y1=[0 for i in range(x)]
x2=[0 for i in range(x)]
y2=[0 for i in range(x)]
o=[0 for i in range(y)]
p=[0 for i in range(y)]
flag=0
flag_1=0
for i in range(x):
    b=input("").split()
    x1[i]=int(b[0])
    y1[i]=int(b[1])
    x2[i]=int(b[2])
    y2[i]=int(b[3])


for i in range(y):
    c=input("").split()
    o[i]=int(c[0])
    p[i]=int(c[1])
    for j in range(x):
        if (x1[j]<=o[i]<=x2[j] and y1[j]<=p[i]<=y2[j]):
            flag+=1
            flag_1=j+1
    if flag>0:
        print("Y {} {}".format(flag,flag_1))
    else:
        print("N")
    flag=0
    flag_1=0