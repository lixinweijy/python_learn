#coding=gbk
from multiprocessing import Process
import os

def func1(name):  #普通一个函数，该函数让子进程调用
    print("当前进程id:",os.getpid())  #getpid()获取当前调用函数的进程ID
    print("父进程id:",os.getppid())  #getppif()获取当前进程的父进程ID
    print("当前进程的名字",name)

#入口
if __name__ == '__main__':
    #创建多个子进程来调用func1函数
    for i in range(5):
        P=Process(target=func1,args=("进程%d"%i,))  #创建一个子进程，传参用元组
        P.start() #开始子进程

    print("父进程代码执行完成")
    #父进程的代码中默认没有任何阻塞，同时父进程必须等待所有子进程结束之后才会结束
