# -*- coding:utf-8 -*-
# a=[]
# for  i in range(4):
#     a.append(str(3))
# print("+".join(a))

num=int(input())
s=[]
for i in range(num):
   s.append(str(num * num -num+1+ i*2))
print(f"{num}*{num}*{num}={num**3}={'+'.join(s)}")
