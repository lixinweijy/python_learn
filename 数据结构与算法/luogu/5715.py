# -*- coding:utf-8 -*-
a=input().split()
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if int(a[i])>int(a[j]):
            a[i],a[j]=a[j],a[i]
for i in range(len(a)):
    print(a[i],end=' ')