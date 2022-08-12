# -*- coding:utf-8 -*-
class Person():
    def __init__(self,xname):
        self.name=xname
        # 斐波拉契数列前两个值是固定的
        self.a,self.b=0,1

    #用于定制对象的描述信息
    def __str__(self):
        return "Person object (name :%s)"%self.name

    #定制对象为可迭代对象，变成可迭代对象需要重写这个函数，必须返回一个迭代器
    def __iter__(self):
        #生成一个斐波拉契数列
        return self

    #重写next可把person变成一个迭代器
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>1000:
            #如果出现一个大于1000的数字就退出循环
            raise StopIteration
        return self.a

    def __getitem__(self, item):#item是一个下标
        if isinstance(item,int):
            a,b=1,1
            for x in range(item):
                a,b=b,a+b
            return a
        elif isinstance(item,slice):
            start=item.start
            stop=item.stop
            if start is None:
                start=0  #start默认值
            a,b=1,1
            L=[]
            for x in range(stop):
                if x>=start:
                    L.append(a)
                a,b=b,a+b
            return L
        else:
            raise "傻逼，出错了"
    #当访问person对象中不存在的属性和函数的时候会抛出AttributeError，如果不想看到这个error则需要重写
    def __getattr__(self, item):
        return "属性名错误"

    def __call__(self, *args, **kwargs):
        print("person对象可以调用")

if __name__ == '__main__':
    p=Person("张三")
    print(p)
    for i in p:
        print(i)
    #这是由于用了__getitem__
    print(p[5])
    # print(p["a"])
    print(p.eat)

    p()  #把person对象当成一个函数直接调用，person对象
    # == 一个函数
