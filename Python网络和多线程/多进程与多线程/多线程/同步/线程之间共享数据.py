# -*- coding:utf-8 -*-

#主线程中的全局变量，作为所有子线程的贡献数据
from threading import Thread
import time
def run_1(num):
    for i in range(10):
        num[0]+=1
    print("线程1，执行之后的结果为:%d"%num[0])
def run_2(num):
    print("线程2，执行之后的结果为:%d"%num[0])

if __name__ == '__main__':
    i=[0] # i 变量为了多个线程可以共享，我们必须使用可变类型
    # i=0
    #创建两个线程
    t1=Thread(target=run_1,args=(i,))
    t2=Thread(target=run_2,args=(i,))
    t1.start()
    time.sleep(1) #延迟一秒钟，保证线程一所有的工作做完
    t2.start()
    print("主线程结束，全局变量g_num的值是:%s"%i)
