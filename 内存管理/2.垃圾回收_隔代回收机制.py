# -*- coding:utf-8 -*-
import sys
import gc
import time
class TestObject(object):
    def __init__(self):
        print("当前对象已经被创建，占用的内存地址为:%s"%hex((id(self))))

    def __del__(self):
        print("当前对象马上被系统回收")
#gc.disable()  #不要启用，这个就禁用gc的垃圾回收功能，python3中gc是默认启用的

while True:
    a = TestObject()
    b = TestObject()
    a.pro = b
    b.pro = a
    del a
    del b
    print(gc.get_threshold())  #打印隔代回收的阈值
    print(gc.get_count())  #打印GC需要回收的对象的数量,到700时就被回收了
    time.sleep(0.1)