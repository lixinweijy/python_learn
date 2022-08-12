#coding=gbk

def test1(func):  # 要求:传的参数是该函数，返回值为一个函数
    def test2():
        print("帮你把饭做好")
        func()
        print("洗碗")
    return test2

@test1 #装饰器
def eat():
    print("我正在吃饭")

# a=test1(eat)
# a()
# 装饰器: 为已经存在的代码添加额外的功能

eat()
print(eat.__name__) # test1