# -*- coding:utf-8 -*-

from  multiprocessing import Pool
import os
import time
#你女儿早读，叫你起床

def test1():
    print("当前进程ID:{0}，他的父进程是:{1}".format(os.getpid(),os.getppid()))
    print("女儿叫你起床，你慢慢开始起床")
    time.sleep(3)
    print("你起床")
    return "abc"


def test2():
    print("女儿开始早读，当前进程是:%s"%os.getpid())
    time.sleep(5)
    print("女儿早读完成")

#test 任务是前面的两个异步任务(test1和test2)，都完成了才调用test3
def test3(args):
    print("最后一起吃早餐，当前进程的id:%s"%os.getpid())
    print("参数是:%s"%args)

if __name__ == '__main__':
    #女儿使用主进程代表
    #父亲使用进程池中某个子进程代表
    #创建进程池
    pool=Pool(4)
    pool.apply_async(func=test1,callback=test3) #callback表示回调函数
    #主进程代表女，叫父亲起床之后，继续早读
    test2()
    print("主进程结束，主进程ID:%s"%os.getpid())