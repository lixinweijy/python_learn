# -*- coding:utf-8 -*-
"""
协程:又称为微线程，纤程。(协程是一种用户态的轻量级线程)
作用:在执行A函数的时候可以随时中断去执行B函数，一个任务遇到IO操作是自动切换到另外一个任务中去，使CPU一直处于就绪状态
"""

from greenlet import greenlet
#开发协程的案例，一个任务是回答，一个任务是问

def ask(name):
    print("%s:我要买个手提包！"%name)
    b.switch("吕布")  #answer函数第一次切换，需要传参
    print("%s:我要学个python！" % name)
    b.switch()

def answer(name):
    print("%s:买买买！！"%name)
    a.switch()
    print("%s:这就买！" % name)

if __name__ == '__main__':
    a = greenlet(ask)  #创建一个协程
    b = greenlet(answer) #创建第二个协程
    a.switch('貂蝉')  # 每个函数只有在第一次切换的时候才需要传参
