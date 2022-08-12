# -*- coding:utf-8 -*-
class Person():
    def say(self,name="hello"):
        print("我说:%s"%name)
"""
第一种方法class
"""
p=Person()  #创建一个Person类的实例
p.say("hello")
print(type(p))  #把实例p的类型打印出来
print(type(Person))  #Person类的类型的打印
#type()函数，使用用于创建类的函数
# type()函数，可以查看一个类型或变量的类型，hello是一个class，他的类型就是type(),而p是一个实例，他的类型就是class

"""
第二种方法type()
"""
# type()函数既可以返回一个对象的类型，又可以创建新的类型
# type(name,bases.dict)
print()
def func(self,worlds='hello'):
    print("我说:%s"%worlds)
#使用type()创建一个Person类
Person = type("Person", (object,), dict(say=func))
p = Person()  # 创建一个Person类的实例
p.say("hello")
print(type(p))  # 把实例p的类型打印出来
print(type(Person))  # Person类的类型的打印

"""
第三种: 使用一个metaclass来创建一个Person类  元类就是来动态创建一个类的
"""
print()
class PersonMetaclass(type):  #所有的元类必须继承type
    def __new__(cls, name,bases,attrs):
        def func(self,words="hello"):
            print("我说:%s"%words)
        attrs['say']=func
        return type.__new__(cls,name,bases,attrs)
#根据上面的元类来创建一个Person类(首先需要一个模具，然后生产产品)
class Person(object,metaclass=PersonMetaclass):
    pass

p = Person()  # 创建一个Person类的实例
p.say("hello")
print(type(p))  # 把实例p的类型打印出来
print(type(Person))  # 打印创建person类的元类
#type是最顶级的元类



a=19
print(int.__class__)
print(a.__class__)              #打印变量a的类型
print(a.__class__.__class__)    #打印变量a的类型的类型  type是所有类型的类型


#第一种写法，通过函数替代元类
def upper_attr(class_name,class_parents,class_attrs):
    # 变量任意一个类的所有属性,把非私有的属性名字写成大写的
    # 定义一个字典保存改完名字之后的属性集合
    new_attrs={}
    for name ,value in class_attrs.items():
        if not name.startswith('__'):# 判断是否为非私有属性
            new_attrs[name.upper()]=value

    #直接调用type来创建一个类
    return type(class_name,class_parents,new_attrs)

#测试
class Emp(object,metaclass=upper_attr):
    name='zhangsan'
    acl=5000

print(hasattr(Emp,'name')) #hasattr  判断Emp类中是否有名字为name的属性
print(hasattr(Emp, 'NAME'))  # hasattr  判断Emp类中是否有名字为name的属性
print(hasattr(Emp, 'ACL'))  # hasattr  判断Emp类中是否有名字为name的属性

print()
#方法二，自己定义了一个元类
class UpperMetaclass(type):
    def __new__(cls,class_name,class_parents,class_attrs):
        new_attrs = {}
        for name, value in class_attrs.items():
            if not name.startswith('__'):  # 判断是否为非私有属性
                new_attrs[name.upper()] = value

        # 直接调用type来创建一个类
        return type.__new__(cls,class_name, class_parents, new_attrs)
class Emp1(object,metaclass=UpperMetaclass):
    name='zhangsan'
    acl=5000
print(hasattr(Emp1,'name')) #hasattr  判断Emp类中是否有名字为name的属性
print(hasattr(Emp1, 'NAME'))  # hasattr  判断Emp类中是否有名字为name的属性
print(hasattr(Emp1, 'ACL'))  # hasattr  判断Emp类中是否有名字为name的属性
