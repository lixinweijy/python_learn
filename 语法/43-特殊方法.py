 # __add__()
a=20
b=100
c=a+b #两个整数类型的对象的相加的操作
d=a.__add__(b)
print(c)
print(d)
class Student:
    def __init__(self,name):
        self.name=name
    def __add__(self, other):
        return self.name+other.name
    def __len__(self):
        return len(self.name)#长度为对象长度

stu1=Student('Jack')
stu2=Student('李四')
# 不能直接相加 需要在上面定义__add__
s=stu1+stu2 #实现了两个对象的加法运算（因为在Student类中编写__add__()特殊的方法）
print(s)
s=stu1.__add__(stu2)
print(s)
# __len__()
print('-------------------------')
lst=[11,22,33,44]
print(len(lst))  # len输出函数的长度
print(lst.__len__())
print(len(stu2))
# __new__() 用于创建对象
class Person(object):

    def __new__(cls, *args, **kwargs):
        print('__new__被调用执行了，cls的id值为{0}'.format(id(cls)))
        obj=super().__new__(cls)
        print('创建的对象的id为:{0}'.format(id(obj)))
        return obj  #return返回给下面的self
#__init__用于初始化对象
    def __init__(self,name,age):
        print('__init__被调用了，self的id值为{0}'.format(id(self)))
        self.name=name
        self.age=age
print("__________________________________________________________")
print('object这个类对象的id为:{0}'.format(id(object)))
print('Person这个类对象的id为:{0}'.format(id(Person)))

#创建Person类的实例对象
p1=Person('张三',20)
# p2=Person("李四",50)
# p3=Person("李四",50)
print('p1这个Person类的实例对象的id:{0}'.format(id(p1)))
# print('p2这个Person类的实例对象的id:{0}'.format(id(p2)))
# print('p3这个Person类的实例对象的id:{0}'.format(id(p3)))

# 大师我悟了！！！！
# new中所创建的对象就是init中的self还有p1
