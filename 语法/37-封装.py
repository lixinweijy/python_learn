 # 提高安全性
class Car:
    def __init__(self,brand):
        self.brand=brand
    def start(self):
        print('汽车已启动...')

car=Car('宝马X5')
car.start()
print(car.brand)
car.start()

# 如果类中的属性不希望在类对象外部被访问，前面使用两个’_‘

class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age #不能在类对象外面使用
    def show(self):
        print(self.name,self.__age)

stu=Student('张三',20)
stu.show()
# 在类的外面使用name与age
print(stu.name)
# print(stu.__age) 报错
print(dir(stu)) #查看stu的类型和方法
print(stu._Student__age) #在类的外部都可以通过_Student__age 进行访问
