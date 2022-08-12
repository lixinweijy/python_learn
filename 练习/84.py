# -*- coding:utf-8 -*-
a=int(input())
b=[]
for i in range(2,a+1):
    if(a%i==0):
        for j in range(2,int(i**1/2)+1):
            if(i%j==0):
                break
        else:
            b.append(str(i))
print(",".join(b))