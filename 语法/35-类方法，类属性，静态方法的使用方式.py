# 对象的创建
class Student:
    native_pace='湖北' #直接写在类里的变量，称为类属性
    def __init__(self,name,age):
        self.name = name
        self.age = age
    # 实例方法
    def eat(self):
        print('学生在吃饭')

    # 静态方法
    @staticmethod
    def method(): #没有self
        print('我使用了staticmethod进行修饰，所以我是静态方法')

    #类方法
    @classmethod
    def cm(cls):
        print('我是类方法，因为我使用了classmethod进行修饰')

print('------------类属性的使用方式-----------')
print(Student.native_pace)
stu1=Student('张三',20)
stu2=Student('李四',30)
print(stu1.native_pace)
print(stu2.native_pace)
Student.native_pace='天津'  #类属性，属性！所有的实例方法所共享
print(stu1.native_pace)
print(stu2.native_pace)
print('------------类方法的使用方式-----------')
Student.cm()
print('------------静态方法的使用方式--------------')
Student.method()