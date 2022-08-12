# 这个文件就是一个模块--包含函数，包含类，包含语句
def fun():
    pass
def fun1():
    pass
# 类中包含类属性，实例方法,类方法，静态方法,实例属性
class Student:
    native_place='吉林' # 类属性
    def eat(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def cm(cls):
        pass
    @staticmethod
    def sm():
        pass

a=10
b=20
print(a+b)

# 模块的导入
import math #关于数学运算
print(id(math))
print(type(math))
print(math)
print(math.pi)
print('------------')
print(dir(math))
print(math.pow(2,3),type(math.pow(2,3)))
print(math.ceil(9.001)) #ceil向上取整
print(math.floor(9.999))#floor向下取整

# 从模块中导入
from math import pi # 导入模块中指定的内容
import math  #导入模块中的所有
print(pi)
print(pow(2,3))
print(math.pow(2,3))

# 可以自己定义函数之后导入，可以隔模块导入
# 不过会报错，需要在目录是点击Mark Directory as  然后点击Sources Root
print('--------------------')
# 以主程序的方法运行
def add(a,b):
    return a+b

if __name__ == '__main__':
    print(add(10,20)) #只有在此模块中运行，不会被引用与别的模块
