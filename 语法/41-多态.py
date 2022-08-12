class Animal:
    def eat(self):
        print('动物会吃')
class Dog(Animal):
    def eat(self):
        print('狗吃骨头')
class Cat(Animal):
    def eat(self):
        print('猫吃鱼')
class Person:
    def eat(self):
        print('人吃五谷杂粮')


# 定义一个函数
def fun(obj):
    obj.eat()

# 开始调用函数
fun(Cat())
fun(Dog())
fun(Animal())
print('---------------')
print(Person())

# 动态语言崇尚鸭子类型，python为动态语言，java为静态语言
# 鸭子类型：不管类别，只管行为
