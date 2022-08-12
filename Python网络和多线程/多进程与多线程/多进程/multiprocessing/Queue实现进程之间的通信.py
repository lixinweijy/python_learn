# -*- coding:utf-8 -*-
from multiprocessing import  Process,Queue
import os
import time

# 创建两个进程，一个负责读，一个负责写

# 负责写的进程
class WriterProcess(Process):
    def __init__(self,xname,mq):
        Process.__init__(self)
        self.name=xname
        self.mq=mq

    def run(self):
        # 把多条数据写入到队列中
        print("进程名字:%s,ID:%s;已经启动"%(self.name,os.getpid()))
        for i in range(1,6):
            self.mq.put(i) #write进程负责把数据写入Queue
            time.sleep(1) #休眠一秒钟
        print("进程名字:%s,ID:%s;已经结束"%(self.name,os.getpid()))

# 负责读的进程
class ReaderProcess(Process):
    def __init__(self,xname,mq):
        Process.__init__(self)
        self.name=xname
        self.mq=mq

    def run(self):
        print("进程名字:%s,ID:%s;已经启动"%(self.name,os.getpid()))
        while(1):
            value=self.mq.get(True)  #当队列中没有数据，改行代码一直堵塞着，里面的True的意思就是是否要阻塞，默认值为True
            print(value)


if __name__ == '__main__':
    q=Queue()
    pw=WriterProcess("write",q)
    pr=ReaderProcess("reader",q)

    #启动两个进程
    pw.start()
    pr.start()

    # 让父进程等待子进程
    pw.join()
    # pr进程是一个死循环
    pr.terminate() #强制杀死pr进程
    print("父进程结束")