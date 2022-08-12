class Person(object): #Person继承object类
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)
        self.stu_no=stu_no

class Teacher(Person):
    def __init__(self,name,age,teachofyear):
        super().__init__(name,age)
        self.teachofyear=teachofyear

stu=Student('张三',20,1001)
teacher=Teacher('李四',34,10)

stu.info()
teacher.info() #info是从Person中继承过来的

# Teacher和Student是Person的两个儿子

# 两个父类
class A(object):
    pass
class B(object):
    pass

class C(A,B): # C有两个爸爸
    pass