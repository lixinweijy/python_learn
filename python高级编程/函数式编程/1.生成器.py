#coding=gbk
import time
# 1
lst1=[1,2,3,4,5,6,7,8,9]
# 2
lst2=[x for x in range(1,10)]

# 生成器:一个对象，保存了产生元素的算法，同时会记录游标的位置
# 创建生成器: 1.通过列表生成器来创建
#           2.通过函数来创建生成器(yield)
# 遍历生成器中的元素内容:
#        1.通过next(g),当生成器中没有数据的时候抛出异常:StopIteration
#        2.通过for循环遍历
#        3.object内置的__next__,当生成器中没有数据的时候抛出异常:StopIteration
#        4.send函数，生成器的第一个值必须使用send(None),后面的值无限制


# 1.通过列表生成器来创建
g=(x for x in range(1,10))
# print(g)
# print(next(g))
# print(next(g))
# print(next(g))
# time.sleep(5)
# print(next(g))
# print(next(g))

next(g)
for i in g:
    print(i,"-----")

g2=(x for x in range(1,10) if x%2==0)
print(next(g2))
print(next(g2))
print(next(g2))
print(next(g2))

print("_____________________________________________________")
def test1(times):
    a,b=0,1
    n= 0
    while n<times:  # yield一般用于创建生成器:工作返回后面的变量值给生成器
        yield b  # print(b)  # b为斐波拉契数列中的一个元素
        a, b = b, (a+b)
        n += 1

g3=test1(6)
for i in g3:
    print(i)

print("_____________________________________________________")
def test2():
    a,b=0,1
    while b<10000:  # yield一般用于创建生成器:工作返回后面的变量值给生成器
        yield b  # print(b)  # b为斐波拉契数列中的一个元素
        a, b = b, (a+b)

g4=test2() # g4代表的是10000以下所有的斐波拉契数列
for i in g4:
    print(i)

# next=__next__
print("______________________________________________________")
# print(g4.send(None))
