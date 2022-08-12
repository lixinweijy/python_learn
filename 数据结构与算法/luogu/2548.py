# -*- coding:utf-8 -*-
a=input().split()
a1=int(a[0])
a2=int(a[1])
b=[0 for i in range(a2)]
for i in range(a2):
    print(1)
    b[i]=input().split()

for j in range(a2):
    for i in range(a1):
        c = b[0][i]
        if b[j][i]!=c:
            b[0][i]="*"
            break

for i in b[0]:
    print(i,end=' ')