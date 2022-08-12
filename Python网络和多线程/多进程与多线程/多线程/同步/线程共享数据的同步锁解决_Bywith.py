# -*- coding:utf-8 -*-
import time
from threading import *

g_num=0

def run():
    print("当前进程%s,开始启动:"%(current_thread().name))
    global g_num
    #获得这把锁的钥匙
    with lock:
        for i in range(500000):
            g_num+=1
    print("线程%s，执行之后g_num的值为:%s"%(current_thread().name,g_num))

if __name__ == '__main__':
    #创建同步锁
    lock=Lock()
    threads=[]
    for i in range(5):
        t=Thread(target=run)
        t.start()
        threads.append(t)
    for j in threads:
        j.join()
    print("主线程结束,g_num的值为:%s"%g_num)
"""
1.加锁还可以使用with，效果一样
2.必须使用同一把锁
3.如果使用锁，程序会变成串行，因此应该在适当的地方加锁(不然影响速度)

"""