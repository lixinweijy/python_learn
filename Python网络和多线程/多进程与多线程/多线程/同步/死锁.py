# -*- coding:utf-8 -*-
import threading
import time
#代表鱼的锁
mutex_Yu=threading.Lock()
#代表熊掌的锁
mutex_XiongZhang=threading.Lock()

class MyThread1(threading.Thread):
    def run(self):
        mutex_Yu.acquire() #得到鱼
        print("线程1已经得到鱼了")
        time.sleep(1)

        mutex_XiongZhang.acquire()
        print("线程1得到熊掌了")
        mutex_XiongZhang.release()
        mutex_Yu.release()

class MyThread2(threading.Thread):
    def run(self):
        mutex_XiongZhang.acquire()
        print("线程2得到熊掌了")
        time.sleep(1)
        mutex_Yu.acquire() #得到鱼
        print("线程2已经得到鱼了")
        mutex_XiongZhang.release()
        mutex_Yu.release()

mutex_heven=threading.RLock()  #Lock()其实是互斥锁，可以使用逻辑锁（RLock），就不会死锁了
class Mythread3(threading.Thread):
    def run(self):
        mutex_heven.acquire()
        print("线程3进入了天堂")
        time.sleep(1)
        self.run()#再次进入天堂
        mutex_heven.release()
if __name__ == '__main__':
    # t1=MyThread1()
    # t2=MyThread2()
    # t1.start()
    # t2.start()
    t3=Mythread3()
    t3.start()
"""
产生死锁的四个必要条件
1.互斥条件:     一个资源每次只能被一个线程使用
2.请求与保持条件:一个线程因请求资源而阻塞时，对已获得的资源保持不放
3.不剥夺条件:    线程已获得的资源，在未使用完之前不能强行剥夺
4.循环等待条件:   若干线程之间形成一种头尾相接的循环等待资源关系
"""