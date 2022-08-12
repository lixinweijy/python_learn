# coding=gbk
# 可迭代对象:可以用for循环遍历的对象  Iterable
# 可用isinstance()判断一个对象是否为Iterable对象
from collections.abc import Iterable
from collections.abc import Iterator

a=(1,)
b=[1,2]
c={}

def test1(arg):
    if isinstance(arg,Iterable):
        print("arg对象是可迭代对象")
    else:
        print("arg对象不是可迭代对象")

test1(b)

# 迭代器:Iterator
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器
def test2(arg):
    if isinstance(arg,Iterator):
        print("arg对象是迭代器")
    else:
        print("arg对象不是迭代器")

test2(b)
# 目前学过的只有生成器是迭代器
test2(a for a in range(5))

# 把list,dict,str变成迭代器
test2(iter(a)) #用iter函数
