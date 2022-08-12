# -*- coding:utf-8 -*-
#同步: 协同步调  串行
#异步: 并行
#线程1，门，每3秒钟需要自动关闭一下。如果有人通过，需要重新刷卡打开
#线程2，人，人通过门，如果门是打开的直接通过，如果没有打开需要刷卡。之后门就已经打开了，通知其他人继续进入
import threading,time,random

event=threading.Event()#创建一个事件
event.set()#设置标志为真，门一开始就是打开的

status=0 #status代表门的状态，如果0~3代表打开，如果等于3就需要关闭

def door():
    global status
    while True:
        print("当前门的状态为:{}".format(status))
        if status>=3:
            print("当前门已经打开了3秒，需要自动关闭")
            event.clear()
        if event.is_set():
            print("当前门是开着的，可以通行!")
            status+=1 #status代表门开始计数
        else:
            print("门已经关了，请用户自己刷卡!")
            event.wait() #门的线程阻塞等待
        time.sleep(1)

def person():
    global  status
    n=0 #人的计数器，看看有多少人进入到门里面
    while True:
        if event.is_set():
            n+=1
            print("门开着，{}号人进入门里面".format(n))
        else:
            print("门关着，{}号人刷卡之后，进入门里面".format(n))
            event.set()
            status=0
        time.sleep(random.randint(1,10))

if __name__ == '__main__':
    d=threading.Thread(target=door)
    p=threading.Thread(target=person)

    d.start()
    p.start()
