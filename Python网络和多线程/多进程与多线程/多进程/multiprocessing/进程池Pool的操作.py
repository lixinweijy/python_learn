# -*- coding:utf-8 -*-
# 一般在一台电脑里面进程数不宜过多
# 进程对减轻简便代码的时间复杂度并没有帮助，这时用多线程好一些

# 使用进程池的优点:
"""
1、提高效率，节省开辟进程和开辟内存空间的时间及销毁进程的时间
2、节省内存空间
"""
# Pool中函数说明:
"""
Pool(num)： 创建多个进程，表示可以同时执行的进程数量。大小是CPU的核心数量
join():     进程池对象调用join，会等待进程池中所有的子进程结束完毕再去结束父进程
close():    如果我们用的是进程池，在调用join()之前必须要先close().并且在close()之后不能再继续往进程池添加新的进程
pool.apply_async(func,args,kwds):   异步指向；讲事件放入到进程池队列。args以元组的方式传参，kwds以字典方式传参
pool.apply_sync(func,args,kwds):    同步执行;将事件放入到进程池队列
"""
# 异步效率高
from multiprocessing.pool import Pool
import os,time
import random

# 打印进程信息，并且记录改进程执行的时长
def run(name):
    start=time.time()
    print("进程名字:%s,ID:%s;已经启动"%(name,os.getpid()))
    time.sleep(random.choice([1,2,3,4,5]))# 进程随机休眠数
    end=time.time()
    print("进程名字:%s,ID:%s;已经结束，耗时%.2f"%(name,os.getpid(),end-start))

if __name__ == '__main__':
    p=Pool(5) #参数默认值是CPU的核心数
    for i in range(10):
        #申请得到一个进程，然后异步调用run函数，非阻塞
        p.apply_async(run,("process"+str(i),))
    p.close()
    p.join()
    print("父进程结束")
# 如果要计算原本不怎么耗时的任务，使用多进程还不如使用单进程耗时短