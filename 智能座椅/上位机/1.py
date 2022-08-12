# -*- coding:utf-8 -*-
import serial
import turtle
import time
import os
from multiprocessing import  Process,Queue
q=Queue()
ser = serial.Serial('COM3', 9600, timeout=1)
print(1)
# 负责写的进程
class WriterProcess(Process):
    def __init__(self,mq):
        Process.__init__(self)
        self.mq=mq
    def run(self):
        # 把数据写入到队列中
        while 1:
            self.mq.put(1) #write进程负责把数据写入Queue
# 负责读的进程
class ReaderProcess(Process):
    def __init__(self,mq):
        Process.__init__(self)
        self.mq=mq
    def run(self):
        while(1):
            value=self.mq.get(True)  #当队列中没有数据，改行代码一直堵塞着，里面的True的意思就是是否要阻塞，默认值为True
            print(2)
read=ReaderProcess(q)
write=WriterProcess(q)
read.start()
write.start()

