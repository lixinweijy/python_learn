# -*- coding:utf-8 -*-
import heapq

def super_number(n,primes):
    ret =1 # 1永远是第一个超级丑数
    hq=[1]  #所有的超级丑数存放列表

    for i in range(n):
        tmp=heapq.heappop(hq) #取出最小的超级丑数

        while hq and hq[0]==tmp:
            heapq.heappop(hq)
        for p in primes:
            heapq.heappush(hq,p*tmp)

        ret =tmp
    return ret

if __name__ == '__main__':
    print(super_number(n=1,primes=[2,7,13,19]))
