# -*- coding:utf-8 -*-
import threading,time,os

class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            print("线程名字:%s,输出:%d"%(self.name,i))
            time.sleep(1)

if __name__ == '__main__':
    start=time.time()
    print("主线程开始时间:%s"%start)
    thread_list=[]
    #创建多个线程
    s="abcdef"
    for i in range(5):
        t=MyThread(name=s[i])#创建线程,里面的参数代表线程名字
        t.start()#启动线程
        thread_list.append(t)
    #等待所有的子线程都停止之后，主线程才终止
    for i in thread_list:
        i.join()#阻塞
    end=time.time()

    print("主线程结束:中间执行的时间为%.2f"%(end-start))
