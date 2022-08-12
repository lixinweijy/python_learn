# -*- coding:utf-8 -*-
"""
协程:又称为微线程，纤程。(协程是一种用户态的轻量级线程)
作用:在执行A函数的时候可以随时中断去执行B函数，一个任务遇到IO操作是自动切换到另外一个任务中去，使CPU一直处于就绪状态
"""

import gevent
#开发协程的案例，一个任务是回答，一个任务是问

def ask(name):
    print("%s:我要买个手提包！"%name)
    gevent.sleep(0)  #人为模拟IO阻塞
    print("%s:我要学个python！" % name)

def answer(name):
    print("%s:买买买！！"%name)
    gevent.sleep(0)  # 人为模拟IO阻塞
    print("%s:这就买！" % name)

if __name__ == '__main__':
    a = gevent.spawn(ask,"小乔")  #创建一个协程
    b = gevent.spawn(answer,"周瑜") #创建第二个协程
    gevent.joinall([a,b])# 自动切换并行执行

