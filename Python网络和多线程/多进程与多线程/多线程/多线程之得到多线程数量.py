# -*- coding:utf-8 -*-
import threading,time,os

class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            print("线程名字:%s,输出:%d"%(self.name,i))
            time.sleep(1)

if __name__ == '__main__':
    print("主线程开始时间:%s"%time.time())
    #创建多个线程
    s="abcdef"
    for i in range(5):
        t=MyThread(name=s[i])#创建线程,里面的参数代表线程名字
        t.start()#启动线程
    while True:
        count=len(threading.enumerate())#获得当前正在运行的线程的数量
        print("当前正在执行的线程数量为:%s"%count)
        if count<=1:
            break
    print("主线程结束")
