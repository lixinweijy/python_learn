# -*- coding:utf-8 -*-
import time
from threading import *

g_num=0

def run():
    #获得这把锁的钥匙
    lock.acquire()
    print("当前进程%s,开始启动:"%(current_thread().name))
    global g_num
    for i in range(500000):
        g_num+=1
    print("线程%s，执行之后g_num的值为:%s"%(current_thread().name,g_num))
    #释放锁
    lock.release()
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
