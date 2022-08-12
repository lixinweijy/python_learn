#coding=gbk
from multiprocessing import Process
import os
import time
class MyProcess(Process):
    def __init__(self,xname):
        Process.__init__(self) #加载父类提供的功能
        self.name=xname

    def run(self):  #子进程在运行过程中执行的函数
        print("当前进程id:", os.getpid())  # getpid()获取当前调用函数的进程ID
        print("父进程id:", os.getppid())  # getppif()获取当前进程的父进程ID
        print("当前进程的名字", self.name)
        time.sleep(3)
if __name__ == '__main__':
    start=time.time()
    process_list=[]
    for i in range(10):
        #创建10个子进程放入一个列表中
        p=MyProcess("process-%d"%(i+1))#创建自定义的函数
        p.start()
        process_list.append(p)  #将子进程放入列表中
    for p in process_list:
        #我们一般都会需要父进程等待所有子进程结束才能执行后面的代码，join等待当前子进程结束
        p.join() #join()是一个堵塞的函数
    #所有子进程结束了
    r=time.time()-start
    print("十个子进程执行的时间是{}".format(r))
# 子进程不能修改父进程中的变量