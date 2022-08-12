# -*- coding:utf-8 -*-
n=int(input(""))
def tao(n):
    if n==1:
        return 1
    else:
        return (tao(n-1)+1)*2
print(tao(n))
