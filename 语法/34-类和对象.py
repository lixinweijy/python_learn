print('---------python中一切皆对象---------')
class Student:  #Student为类的名称，类名由一个或者多个单词组成，首字母大写，其余小写
    pass

# python中一切皆对象，Student是对象吗？内存有开空间吗？
print(id(Student))
print(type(Student))
print(Student)
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

# 在类之外定义的称为函数，在类之内定义的称为方法
def drink():
    print('喝水')

stu1=Student('张三',20)
print(id(stu1))
print(type(stu1))
print(stu1)

stu1.eat()
stu1.method()
drink()
print(stu1.name)
print(stu1.age)

print('------------------')
Student.eat(stu1)  #40行与33行效果相同
                   # 类名，方法名（类的对象）--》实际上就是方法定义处的self
