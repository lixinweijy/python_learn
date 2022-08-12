# -*- coding:utf-8 -*-
import math
a=int(input(""))
z=[]
for i in range(a):
    m=int(input(""))
    n=input()
    z.append(n)
def zifu(k):
    a=k.split()
    flag=1
    while flag:
        flag=0
        for i in range(len(a)):
            for j in range(i+1,len(a)):
                if ord(a[i])==ord(a[j])+17 or ord(a[i])==ord(a[j])+6 or ord(a[i])==ord(a[j])-17 or ord(a[i])==ord(a[j])-6:
                    a.pop(j)
                    a.pop(i)
                    flag+=1
                    print(1)
                    break
    flag1=1
    flag2=1
    for i in a:
        if i=="U" or i=="D":
            flag1+=1
        else:
            flag2+=1
    b=flag1**2+flag2**2
    b=math.sqrt(b)
    return b
for i in z:
    print(zifu(i))