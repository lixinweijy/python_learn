# -*- coding:utf-8 -*-
a = int(input(""))
b = input("").split()
c = []
for i in range(a):
    c.append(int(b[i]))


def num(z):
    d = 0
    while (z >= 10):
        d += z % 10
        z = z / 10
    d += z
    if d >= 10:
        num(d)
    else:
        return d


for i in range(len(c)):
    c[i] = num(i)


def num_1(flag, k, g, x):
    for j in range(g, x):
        k += c[j]
        k = num(k)
        if k == i:
            flag += 1
        if j==x-1:
            return flag
        g=j+1
        num_1(flag, k, g, x)
        return flag


for i in range(1, 10):
    flag = 0
    g = 0
    k = 0
    o=num_1(flag, k, g, len(c))
    print(o % 998244353, end=" ")

