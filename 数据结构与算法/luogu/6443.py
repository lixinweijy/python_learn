# -*- coding:utf-8 -*-
a=input().split()
a1=int(a[0])
a2=int(a[1])
a3=int(a[2])
b=0
for i in range(1,(a1+a2-a3)//3+1):
    if (a1-i*2>=0 and a2-i>=0 and a1+a2-3*i-a3>=0):
        b=i
print(b)
