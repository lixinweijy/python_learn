# -*- coding:utf-8 -*-
import math
a=int(input(""))
b=input().split()
print(b)
k=0
for i in range(a):
    for j in range(i,a):
        k+=math.fabs(int(b[i])+int(b[j])-1000)
print(k)