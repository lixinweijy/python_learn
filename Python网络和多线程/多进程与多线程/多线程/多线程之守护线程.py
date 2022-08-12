# -*- coding:utf-8 -*-
import threading,time,os

class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            print("线程名字:%s,输出:%d"%(self.name,i))
            time.sleep(1)
if __name__ == '__main__':
    print("主线程开始时间:%s"%time.time())
    #创建一个线程
    t=MyThread(name="my_thread")#创建线程,里面的参数代表线程名字
    t.setDaemon(True)#当前子线程设置为守护线程
    #t.daemon=True 和上面的代码一样
    t.start()#启动线程
    time.sleep(1)
    print("主线程结束")
#守护线程:主线程一结束，守护进程不管有没有结束都要终止
"""
1.每一个线程都会有一个名字，python会自动为线程指定一个名字
2.当线程的run()方法结束时该线程完成
3.无法控制线程调度程序，但是可以通过其他方式来影响线程调度的方式
4.线程的几种状态:新建->就绪->运行->等待(阻塞)->终止(死亡)
"""