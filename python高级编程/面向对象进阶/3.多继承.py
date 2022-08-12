# -*- coding:utf-8 -*-
class Father():
    def work(self):
        print("父亲在工作")

class Mather():
    def work(self):
        print("母亲在工作")

class Child(Father,Mather):  #多继承
    def __init__(self,xname):
        self.name=xname
    def work(self):
        print(self.name+"在工作")

lxw=Child("李新伟")
lxw.work()   #如果多个父类中都有同样的函数，按照优先级调用
print(Child.__mro__)  #打印child的继承结构，并且按照优先级
