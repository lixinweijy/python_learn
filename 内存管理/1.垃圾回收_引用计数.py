# -*- coding:utf-8 -*-
import sys
class TestObject():
    def __init__(self):
        print("当前对象已经被创建，占用的内存地址为:%s"%hex(id(self)))

a=TestObject()
b=a
list1=[]
list1.append(a)
print("当前对象的引用计数为:%s"%sys.getrefcount(a))  #调用这个函数的时候加了一个引用

"""
增加引用计数
a.对象被创建
b.另外变量也指向当前对象
c.作为容器对象的一个元素
d.作为参数提供给函数:test(x)
"""

"""
减少引用计数
a.变量被显示的销毁
b.对象的另一个变量重新赋值
c.从容器中移除
d.函数被执行完毕
"""

# 减少
# del a
b=1000
list1.remove(a)
print("当前对象的引用计数为:%s"%sys.getrefcount(a))  #调用这个函数的时候加了一个引用
#如果引用被删除，引用计数为0了，该对象就会被垃圾回收

