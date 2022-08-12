# -*- coding:utf-8 -*-
# 两端通信
"""
1、send（obj）：
发送一个obj给管道的另一端，另一端用recv()方法接收，需要说明的是，该obj必须是可序列化的，如果该对象序列化之后超过32MB，则很可能引发ValueError异常
2、recv():
接收另一端通过send()方法过来的数据
3、close():
关闭连接
4、poll(timeout)
返回连接中是否还有数据可以读取
5、send_byte(buffer[,offset[,size]])
发送字节数据，如果没有指定得到offset，size参数，则默认发送buffer字节串的全部数据；如果指定来offset和size参数，则只发送buffer字节串中从offset开始、长度为size的字节数据，通过该方法发送的数据，应该使用recv_byte()或recv_bytes_into方法接收。
6、recv_bytes([maxlength])
接收通过send_byte()方法发送的数据，maxlength指定最多接收的字节数，该方法返回接收到的字节数据
7、recv_bytes_into(buffer[,offset])
功能与recv_bytes()方法类似，只是该方法将接收到的数据放在buffer中
"""
from multiprocessing import  Process,Pipe
import os,time

# 创建两个进程，一个负责读，一个负责写

# 负责写的进程
class WriterProcess(Process):
    def __init__(self,xname,pipe):
        Process.__init__(self)
        self.name=xname
        self.pipe=pipe

    def run(self):
        # 把多条数据写入到队列中
        print("进程名字:%s,ID:%s;已经启动"%(self.name,os.getpid()))
        for i in range(1,6):
            self.pipe.send(i) #write进程负责把数据通过管道发送给另外一个进程
            time.sleep(1) #休眠一秒钟
        print("进程名字:%s,ID:%s;已经结束"%(self.name,os.getpid()))

# 负责读的进程
class ReaderProcess(Process):
    def __init__(self,xname,pipe):
        Process.__init__(self)
        self.name=xname
        self.pipe=pipe

    def run(self):
        print("进程名字:%s,ID:%s;已经启动"%(self.name,os.getpid()))
        while(1):
            value=self.pipe.recv()  #当管道中没有数据，该行代码一直堵塞着
            print(value)

if __name__ == '__main__':
    p1,p2=Pipe()  #Pipe创建之后得到管道的两端
    pw=WriterProcess("write",p1)
    pr=ReaderProcess("reader",p2)

    #启动两个进程
    pw.start()
    pr.start()

    # 让父进程等待子进程
    pw.join()
    # pr进程是一个死循环
    pr.terminate() #强制杀死pr进程
    print("父进程结束")